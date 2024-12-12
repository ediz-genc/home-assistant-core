import pytest
from homeassistant.core import HomeAssistant
from homeassistant.const import STATE_ON, STATE_OFF
from homeassistant.components.media_player import DOMAIN as MEDIA_PLAYER_DOMAIN
from homeassistant.components.input_boolean import DOMAIN as INPUT_BOOLEAN_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.helpers import entity_registry
from datetime import timedelta
from homeassistant.util.dt import utcnow
from homeassistant.helpers.event import async_fire_time_changed


# Part 1.1   Function: Reduce volume when power saving mode is enabled
@pytest.mark.asyncio
async def test_eco_mode_volume_adjustment(hass: HomeAssistant):
    """
    Test the functionality of Eco Mode's interaction with the Energy Management System:
    - With Eco Mode enabled, the volume was adjusted to 80% and played for 10 hours to verify that the energy saving values were updated correctly.
    - With Eco Mode turned off, the volume returns to 100% and the playback time no longer increases the energy savings value.
    """

    media_player_entity_id = "media_player.spotify_player"
    eco_mode_entity_id = "input_boolean.eco_mode"
    
    hass.states.async_set(eco_mode_entity_id, STATE_OFF)
    await hass.async_block_till_done()
    state = hass.states.get(media_player_entity_id)
    assert state is not None, "not exist"
    volume_level = state.attributes.get("volume_level")
    assert volume_level == 1.0, f"{volume_level}"

    # turn on Eco Mode
    hass.states.async_set(eco_mode_entity_id, STATE_ON)
    await hass.async_block_till_done()
    state = hass.states.get(media_player_entity_id)
    volume_level = state.attributes.get("volume_level")
    assert volume_level == 0.8, f"{volume_level}"

    # turn off Eco Mode
    hass.states.async_set(eco_mode_entity_id, STATE_OFF)
    await hass.async_block_till_done()
    state = hass.states.get(media_player_entity_id)
    volume_level = state.attributes.get("volume_level")
    assert volume_level == 1.0, f"{volume_level}"


# Part 1.2 Energy Management System Interaction (Also Intergration Test)
@pytest.mark.asyncio
async def test_eco_mode_energy_saving(hass: HomeAssistant):
    """
    Test the functionality of Eco Mode's interaction with the Energy Management System:
    - With Eco Mode enabled, the volume was adjusted to 80% and played for 10 hours to verify that the energy saving values were updated correctly.
    - When Eco Mode is turned off, the volume is restored to 100% and the playback time no longer increases the energy saving value.
    """
    eco_mode_entity_id = "input_boolean.eco_mode"
    media_player_entity_id = "media_player.spotify_player"
    energy_saving_sensor_id = "sensor.energy_saving"
    
    hass.states.async_set(eco_mode_entity_id, STATE_OFF)
    hass.states.async_set(media_player_entity_id, {
        "state": "playing",
        "volume_level": 1.0  # 100%
    })
    hass.states.async_set(energy_saving_sensor_id, 0.0)  
    
    await hass.async_block_till_done()
    
    # turn on Eco Mode
    hass.states.async_set(eco_mode_entity_id, STATE_ON)
    await hass.async_block_till_done()
    state = hass.states.get(media_player_entity_id)
    assert state is not None, "Player do not exsit"
    assert state.attributes.get("volume_level") == 0.8, "Eco Mode volume 80%"
    ENERGY_SAVING_PER_HOUR = 10.0
    
    for hour in range(10):
        future_time = hass.helpers.event.async_track_time_change(
            hass, lambda now: None, hour=hour+1
        )
        hass.bus.async_fire("time_changed", {"now": hass.config.time().replace(hour=(hour+1) % 24)})
        await hass.async_block_till_done()
        expected_energy_saving = ENERGY_SAVING_PER_HOUR * (hour + 1)
        energy_state = hass.states.get(energy_saving_sensor_id)
        assert energy_state is not None, "energy_saving entity does not exist"
        assert energy_state.state == str(expected_energy_saving), f"{hour + 1}save{expected_energy_saving}"
    
    # turn off Eco Mode
    hass.states.async_set(eco_mode_entity_id, STATE_OFF)
    await hass.async_block_till_done()
    state = hass.states.get(media_player_entity_id)
    assert state.attributes.get("volume_level") == 1.0, "Eco Mode volume 100%"
    for hour in range(5):
        future_time = hass.helpers.event.async_track_time_change(
            hass, lambda now: None, hour=hour+11
        )
        hass.bus.async_fire("time_changed", {"now": hass.config.time().replace(hour=(hour + 11) % 24)})
        await hass.async_block_till_done()
        energy_state = hass.states.get(energy_saving_sensor_id)
        assert energy_state.state == str(ENERGY_SAVING_PER_HOUR * 10), "no more saving power"

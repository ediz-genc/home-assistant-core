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

# Part 3.1  Function: Statistical playback time
@pytest.mark.asyncio
async def test_spotify_listening_time(hass):

    hass.states.async_set("switch.spotify_usage", "off")
    await hass.async_block_till_done()

    state = hass.states.get("sensor.spotify_listening_time")
    assert state is not None
    assert float(state.state) == 0.0
    hass.states.async_set("switch.spotify_usage", "on")
    await hass.async_block_till_done()

    future_time = utcnow() + timedelta(hours=1)
    async_fire_time_changed(hass, future_time)
    await hass.async_block_till_done()

    state = hass.states.get("sensor.spotify_listening_time")
    assert float(state.state) == pytest.approx(1.0, 0.1)

    hass.states.async_set("switch.spotify_usage", "off")
    await hass.async_block_till_done()

    future_time = utcnow() + timedelta(hours=1.5)
    async_fire_time_changed(hass, future_time)
    await hass.async_block_till_done()

    state = hass.states.get("sensor.spotify_listening_time")
    assert float(state.state) == pytest.approx(1.0, 0.1)





# Part 3.2.1 Carbon Footprint Calculation, Validation of Calculation for Only One Mode
import pytest
@pytest.mark.asyncio
async def test_spotify_carbon_footprint_calculation(hass):
    """
    - Input: playback time and estimated carbon emissions modelling.
    - Output: verify that sensor.spotify_carbon_footprint is updated correctly.
    """
    hass.states.async_set("sensor.spotify_listening_time", "60")
    hass.states.async_set(
        "input_text.spotify_media_player",
        "media_player.spotify_jialong_he",
        {"volume_level": 0.8}
    )

    #Spotify mode = Relaxation
    hass.states.async_set("input_select.spotify_mode", "Relaxation")
    await hass.async_block_till_done()

    state = hass.states.get("sensor.spotify_carbon_footprint")
    assert state is not None

    # Formula: (volume+1)*listening_time*multiplier = (0.8+1)*60*0.02 = 1.8*60*0.02=2.16
    assert state.state == "2.16"



#  Part 3.2.2 Carbon Footprint Calculation, Validation of Calculation for Different Mode
@pytest.mark.asyncio
@pytest.mark.parametrize("mode,multiplier,expected", [
    ("Relaxation", 0.02, 2.16),
    ("Gym", 0.03, 3.24),
    ("Cooking", 0.015, 1.62),
    ("Study", 0.01, 1.08),
    ("Unknown", 0.02, 2.16), 
])
async def test_spotify_carbon_footprint_modes(hass, mode, multiplier, expected):
    listening_time = 60.0
    volume = 0.8

    hass.states.async_set("sensor.spotify_listening_time", str(listening_time))
    hass.states.async_set(
        "input_text.spotify_media_player",
        "media_player.spotify_jialong_he",
        {"volume_level": volume}
    )
    hass.states.async_set("input_select.spotify_mode", mode)
    await hass.async_block_till_done()
    state = hass.states.get("sensor.spotify_carbon_footprint")
    assert state is not None, "sensor.spotify_carbon_footprint should exist."
    assert state.state == f"{expected}", f"Mode: {mode}, Expected: {expected}, Got: {state.state}"

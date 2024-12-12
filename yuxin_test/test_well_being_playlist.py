import pytest
from homeassistant.core import HomeAssistant
from homeassistant.const import STATE_ON, STATE_OFF, MEDIA_TYPE_PLAYLIST
from homeassistant.components.input_button import DOMAIN as INPUT_BUTTON_DOMAIN
from homeassistant.components.input_text import DOMAIN as INPUT_TEXT_DOMAIN
from homeassistant.setup import async_setup_component
from datetime import timedelta

@pytest.mark.asyncio
async def test_well_being_playlist_play_media(hass: HomeAssistant):
    """
    Test the Well-Being Playlist function:
    - Presses the Play button to invoke the playback service, specifying the playlist URI.
    - Verify that the correct URI is used.
    - Verify that random play and repeat play are disabled.
    """
    
    well_being_playlist_button = "input_button.well_being_playlist"
    spotify_device_id_entity = "input_text.spotify_device_id"
    spotify_media_player = "media_player.spotify_yuxin_guo"
    hass.states.async_set(spotify_device_id_entity, "19dcae4c19ef2bc79843c67c32880993464d8ca8")
    hass.states.async_set(spotify_media_player, {
        "state": "off",
        "volume_level": 0.8 
    })
    hass.states.async_set("input_select.spotify_mode", "Gym")
    hass.states.async_set("input_boolean.eco_mode", STATE_OFF)
    
    await hass.async_block_till_done()
    
    # URI（Gym）
    expected_playlist_uri = "spotify:playlist:37i9dQZF1DXdxcBWuJkbcy"  
    service_calls = []

    async def spotcast_start_listener(call):
        service_calls.append(call)
    
    hass.services.async_register("spotcast", "start", spotcast_start_listener)
 
    automation_config = {
        "alias": "Play Well-Being Playlist on Button Press",
        "trigger": [
            {
                "platform": "event",
                "event_type": "call_service",
                "event_data": {
                    "domain": INPUT_BUTTON_DOMAIN,
                    "service": "press",
                    "service_data": {
                        "entity_id": well_being_playlist_button
                    }
                }
            }
        ],
        "action": [
            {
                "service": "spotcast.start",
                "data": {
                    "uri": expected_playlist_uri,
                    "force_playback": True,
                    "spotify_device_id": "{{ states('input_text.spotify_device_id') }}",
                    "shuffle": False,
                    "random_song": False
                }
            }
        ]
    }
    
    assert await async_setup_component(hass, "automation", {"automation": [automation_config]})
    await hass.async_block_till_done()
    
    # Turn on Well-Being Playlist 
    await hass.services.async_call(
        INPUT_BUTTON_DOMAIN,
        "press",
        {"entity_id": well_being_playlist_button},
        blocking=True,
    )
    await hass.async_block_till_done()
    assert len(service_calls) == 1, "spotcast.start doesnot work"
    
    call = service_calls[0]
    assert call.domain == "spotcast", f"real '{call.domain}'"
    assert call.service == "start", f"real '{call.service}'"

    service_data = call.data
    assert service_data["uri"] == expected_playlist_uri, f" {expected_playlist_uri}，real URI {service_data.get('uri')}"
    assert service_data.get("shuffle") == False, "shuffle should be banned"
    assert service_data.get("random_song") == False, "random_song should be banned"
    assert service_data.get("force_playback") == True, "force_playback should be actived"
    assert service_data.get("spotify_device_id") == "19dcae4c19ef2bc79843c67c32880993464d8ca8", "Spotify device ID wrong"
    
    hass.states.async_set(spotify_media_player, "playing", {"volume_level": 0.8})
    await hass.async_block_till_done()
    
    state = hass.states.get(spotify_media_player)
    assert state.state == "playing", "status 'playing'"
    assert state.attributes.get("volume_level") == 0.8, "volume 80%"

    assert not state.attributes.get("shuffle", True), "shuffle should be banned"
    assert state.attributes.get("repeat") == "off", "repeat should be banned"

import asyncio
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_COUNTRY
from .media_player import setup_media_player
from .sensor import setup_sensors
from .switch import setup_switches
from .automation import setup_automations
from .services import setup_services

DOMAIN = "spotify"

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    sp_dc = entry.data.get("sp_dc")
    sp_key = entry.data.get("sp_key")
    country = entry.data.get(CONF_COUNTRY, "SE")
    spotify_client = SpotifyClient(sp_dc=sp_dc, sp_key=sp_key, country=country)
    await spotify_client.initialize()
    hass.data[DOMAIN][entry.entry_id] = {
        "spotify_client": spotify_client
    }
    await asyncio.gather(
        setup_media_player(hass, entry),
        setup_sensors(hass, entry),
        setup_switches(hass, entry),
        setup_automations(hass, entry),
        setup_services(hass, entry),
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.debug("Unloading Spotify config entry")
    unload_ok = await asyncio.gather(
        hass.config_entries.async_forward_entry_unload(entry, "media_player"),
        hass.config_entries.async_forward_entry_unload(entry, "sensor"),
        hass.config_entries.async_forward_entry_unload(entry, "switch"),
    )
    if all(unload_ok):
        spotify_client = hass.data[DOMAIN][entry.entry_id]["spotify_client"]
        await spotify_client.cleanup()
        hass.data[DOMAIN].pop(entry.entry_id)
        return True
    return False

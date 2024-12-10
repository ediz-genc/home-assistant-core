# noqa: ignore=all


"""Spotify Instance Data - `instancedata_spotify.py`.

This module defines the `InstanceDataSpotify` dataclass, which serves as a container for instance-specific data
and configuration required by the Spotify integration in Home Assistant. It centralizes the management of critical
objects and settings, ensuring consistent access across various components.

Key Features:
- **Centralized Data Storage**:
  - Manages Spotify Connect devices, media player entities, OAuth2 sessions, and configuration options.
  - Designed for use by other integration components to simplify data access and management.
- **Device and Playback Options**:
  - Provides properties for default Spotify Connect device credentials and behavior.
  - Includes configuration for hiding devices in the source list and managing device power states through scripts.
- **Integration with Home Assistant**:
  - Leverages Home Assistant's `DataUpdateCoordinator` for refreshing device data.
  - Utilizes `OAuth2Session` for secure API communication with Spotify.

Attributes:
- `devices`: A `DataUpdateCoordinator` instance that manages a list of Spotify Connect devices.
- `media_player`: The media player entity controlling Spotify playback.
- `options`: A read-only mapping of configuration options.
- `session`: The OAuth2 session for Spotify Web API interactions.
- `spotifyClient`: A Spotify client instance for API communication.

Properties:
- `OptionDeviceDefault`: The default Spotify Connect player device.
- `OptionDeviceLoginId`: The login ID for connecting to inactive devices.
- `OptionDevicePassword`: The password for connecting to inactive devices.
- `OptionDeviceUsername`: The username for connecting to inactive devices.
- `OptionScriptTurnOff`: Script ID to power off devices.
- `OptionScriptTurnOn`: Script ID to power on devices.
- `OptionSourceListHide`: A list of devices to hide from the source list.

Usage:
The `InstanceDataSpotify` class is instantiated in `__init__.py` and accessed throughout the integration to
streamline data handling and ensure consistency.

Notes:
- The `OptionSourceListHide` property processes a semi-colon-delimited string to return a list of normalized
device identifiers.
- Refresh intervals for `devices` are managed by the `DataUpdateCoordinator` and can be customized based on the
integration's requirements.

"""

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any

from spotifywebapipython import SpotifyClient
from spotifywebapipython.models import SpotifyConnectDevices

from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import (
    CONF_OPTION_DEVICE_DEFAULT,
    CONF_OPTION_DEVICE_LOGINID,
    CONF_OPTION_DEVICE_PASSWORD,
    CONF_OPTION_DEVICE_USERNAME,
    CONF_OPTION_SCRIPT_TURN_OFF,
    CONF_OPTION_SCRIPT_TURN_ON,
    CONF_OPTION_SOURCE_LIST_HIDE,
)


@dataclass
class InstanceDataSpotify:
    """Spotify instance data stored in the Home Assistant data object.

    This contains various attributes and object instances that the integration needs
    to function.  It is created in `__init__.py`, and referenced in various other
    modules.
    """

    devices: DataUpdateCoordinator[SpotifyConnectDevices]
    """
    List of Spotify Connect devices that are available.
    This property is refreshed every 5 minutes by a DataUpdateCoordinator.
    """

    media_player: MediaPlayerEntity
    """
    The media player instance used to control media playback.
    """

    options: MappingProxyType[str, Any]
    """
    Configuration entry options.
    """

    session: OAuth2Session
    """
    The OAuth2 session used to communicate with the Spotify Web API.
    """

    spotifyClient: SpotifyClient
    """
    The SpotifyClient instance used to interface with the Spotify Web API.
    """

    @property
    def OptionDeviceDefault(self) -> str | None:
        """The default Spotify Connect player device."""
        return self.options.get(CONF_OPTION_DEVICE_DEFAULT, None)

    @property
    def OptionDeviceLoginId(self) -> str | None:
        """The default Spotify Connect loginid to use when connecting to an inactive device."""
        return self.options.get(CONF_OPTION_DEVICE_LOGINID, None)

    @property
    def OptionDevicePassword(self) -> str | None:
        """The default Spotify Connect password to use when connecting to an inactive device."""
        return self.options.get(CONF_OPTION_DEVICE_PASSWORD, None)

    @property
    def OptionDeviceUsername(self) -> str | None:
        """The default Spotify Connect username to use when connecting to an inactive device."""
        return self.options.get(CONF_OPTION_DEVICE_USERNAME, None)

    @property
    def OptionScriptTurnOff(self) -> str | None:
        """Script entity id that will be called to power off the device that plays media content."""
        return self.options.get(CONF_OPTION_SCRIPT_TURN_OFF, None)

    @property
    def OptionScriptTurnOn(self) -> str | None:
        """Script entity id that will be called to power on the device that plays media content."""
        return self.options.get(CONF_OPTION_SCRIPT_TURN_ON, None)

    @property
    def OptionSourceListHide(self) -> list:
        """The list of devices to hide from the source list."""
        result: list = []

        # get option value.
        value: str = self.options.get(CONF_OPTION_SOURCE_LIST_HIDE, None)

        # build a list from the semi-colon delimited string.
        if value is not None:
            result = value.split(";")
            for idx in range(len(result)):
                result[idx] = result[idx].strip().lower()

        # return result.
        return result

# noqa: ignore=all

"""Spotify Integration Constants - `const.py`.

This module defines constants used throughout the Spotify integration in Home Assistant. These constants
standardize key identifiers, configuration options, logging, and API requirements, ensuring consistency and
 maintainability across the integration.

Key Features:
- **Domain and Logger**:
  - `DOMAIN`: Identifier for the Spotify integration.
  - `LOGGER`: Configured logger for the integration, scoped to its package.

- **Configuration Options**:
  - Constants for user-configurable options, such as default devices, credentials, and script actions for turning
    devices on and off.
  - `CONF_OPTION_DEVICE_DEFAULT`, `CONF_OPTION_DEVICE_LOGINID`, `CONF_OPTION_SCRIPT_TURN_ON`, etc.

- **Spotify Web API Scopes**:
  - `SPOTIFY_SCOPES`: A comprehensive list of security scopes required for accessing various Spotify Web API endpoints.
  - Includes scopes for managing playlists, playback state, user libraries, and more.

- **Specialized Trace Messages**:
  - `TRACE_MSG_DELAY_DEVICE_SONOS`: Custom trace message to handle delays for Sonos devices when interacting with
  Spotify playback.

Attributes:
- `DOMAIN`: Specifies the unique identifier for the Spotify integration in Home Assistant.
- `DOMAIN_SCRIPT`: Defines the domain identifier for script integration.
- `SPOTIFY_SCOPES`: A list of OAuth2 permission scopes for Spotify Web API access.

Usage:
These constants are used throughout the integration to define domain identifiers, configuration keys, logging, and API
interaction requirements.

Notes:
- The `SPOTIFY_SCOPES` list should be updated if Spotify introduces new API features requiring additional permissions.
- The trace message for Sonos delays (`TRACE_MSG_DELAY_DEVICE_SONOS`) is specialized for scenarios involving playback
state changes with Sonos devices.

"""

"""
Constants for the Spotify component.
"""

import logging

DOMAIN = "spotify"
""" Domain identifier for this integration. """

DOMAIN_SCRIPT = "script"
""" Domain identifier for script integration. """

LOGGER = logging.getLogger(__package__)

CONF_OPTION_DEVICE_DEFAULT = "device_default"
CONF_OPTION_DEVICE_LOGINID = "device_loginid"
CONF_OPTION_DEVICE_PASSWORD = "device_password"
CONF_OPTION_DEVICE_USERNAME = "device_username"
CONF_OPTION_SCRIPT_TURN_ON = "script_turn_on"
CONF_OPTION_SCRIPT_TURN_OFF = "script_turn_off"
CONF_OPTION_SOURCE_LIST_HIDE = "source_list_hide"

# security scopes required by various Spotify Web API endpoints.
SPOTIFY_SCOPES: list = [
    "playlist-modify-private",
    "playlist-modify-public",
    "playlist-read-collaborative",
    "playlist-read-private",
    "ugc-image-upload",
    "user-follow-modify",
    "user-follow-read",
    "user-library-modify",
    "user-library-read",
    "user-modify-playback-state",
    "user-read-currently-playing",
    "user-read-email",
    "user-read-playback-position",
    "user-read-playback-state",
    "user-read-private",
    "user-read-recently-played",
    "user-top-read",
]

TRACE_MSG_DELAY_DEVICE_SONOS: str = (
    "Delaying for %s seconds to allow Sonos Soco API to process the change"
)
"""
Delaying for %s seconds to allow Sonos Soco API to process the change
"""

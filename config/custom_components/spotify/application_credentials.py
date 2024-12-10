# noqa: ignore=all

"""Spotify Application Credentials Component - `application_credentials.py`.

This module provides the application credentials platform for the Spotify integration in Home Assistant. It enables
secure authorization with Spotify's Web API by defining an `AuthorizationServer` instance for OAuth2 flows.

Key Features:
- Defines the Spotify authorization server, including:
  - Authorization URL: `https://accounts.spotify.com/authorize`
  - Token URL: `https://accounts.spotify.com/api/token`
- Facilitates OAuth2 authentication for Spotify API access within the Home Assistant ecosystem.
- Integrates SmartInspect logging for debugging and tracking the creation of authorization server objects.

Dependencies:
- `homeassistant.components.application_credentials`: For managing credentials securely.
- `smartinspectpython.siauto`: For advanced logging and monitoring.
- `DOMAIN`: Integration-specific constants.

Usage:
The `async_get_authorization_server` function initializes and returns an instance of `AuthorizationServer`, which is
used to handle Spotify's OAuth2 process.

Note:
Ensure SmartInspect logging is properly configured to utilize detailed debugging capabilities. If unavailable, fallback
logging will still capture key events.

"""

"""Application credentials platform for spotify."""

import logging

# get smartinspect logger reference; create a new session for this module name.
from smartinspectpython.siauto import SIAuto, SILevel, SISession

from homeassistant.components.application_credentials import AuthorizationServer
from homeassistant.core import HomeAssistant

_logsi: SISession = SIAuto.Si.GetSession(__name__)
if _logsi == None:
    _logsi = SIAuto.Si.AddSession(__name__, True)
_logsi.SystemLogger = logging.getLogger(__name__)


async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer:
    """Return authorization server."""
    # create a new authorization server instance for Spotify Web API usage.
    auth_server: AuthorizationServer = AuthorizationServer(
        authorize_url="https://accounts.spotify.com/authorize",
        token_url="https://accounts.spotify.com/api/token",
    )

    _logsi.LogObject(
        SILevel.Verbose, "Component AuthorizationServer object", auth_server
    )
    return auth_server

# noqa: ignore=all

"""Spotify System Health Component - `system_health.py`.

This module provides system health information for the Spotify integration in Home Assistant. It is designed to monitor
and report on the integration's status, configuration, and connectivity to ensure smooth operation and assist with troubleshooting.

Key Features:
- **System Health Registration**:
  - Registers the system health callback to display integration-specific information on the system health page in Home Assistant.
- **Integration Information**:
  - Reports the integration version by reading the `manifest.json` file.
- **Client Configuration Details**:
  - Lists the Spotify clients configured, including user profiles and associated product types.
- **API Connectivity Check**:
  - Verifies whether the Spotify Web API endpoint is reachable.
- **Trace Logging**:
  - Leverages SmartInspect logging for detailed diagnostics and traceability.

Functions:
- `async_register`: Registers the system health callback for the Spotify integration.
- `system_health_info`: Collects and returns health information for display on the system health page.
- `_getManifestFile`: Reads and parses the integration's `manifest.json` file to retrieve version information.

Attributes:
- `DOMAIN`: The domain identifier for the Spotify integration.
- `InstanceDataSpotify`: Provides access to client-specific data stored in Home Assistant's data registry.

Usage:
This component is automatically invoked during the integration setup process. The collected system health information can be
accessed via Home Assistant's system health page, offering insights into the integration's current state.

Notes:
- The `manifest.json` file must exist and be accessible in the expected path under the Home Assistant configuration directory.
- Any exceptions during the health information gathering process are logged and raised, ensuring visibility for debugging.
- API connectivity checks rely on Home Assistant's `system_health.async_check_can_reach_url` utility for asynchronous verification.

"""

"""Provide info to system health."""

import json
import logging
from typing import Any

# get smartinspect logger reference; create a new session for this module name.
from smartinspectpython.siauto import SIAuto, SILevel, SISession

from homeassistant.components import system_health
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN
from .instancedata_spotify import InstanceDataSpotify

_logsi: SISession = SIAuto.Si.GetSession(__name__)
if _logsi == None:
    _logsi = SIAuto.Si.AddSession(__name__, True)
_logsi.SystemLogger = logging.getLogger(__name__)


@callback
def async_register(
    hass: HomeAssistant, register: system_health.SystemHealthRegistration
) -> None:
    """Register system health callbacks."""
    register.async_register_info(
        system_health_info, "/config/integrations/integration/%s" % DOMAIN
    )


async def system_health_info(hass):
    """Get info for the info page."""

    try:
        # trace.
        _logsi.EnterMethod(SILevel.Debug)

        # create dictionary for health information.
        healthInfo: dict[str, Any] = {}

        # add manifest file details.
        # as of HA 2024.6, we have to use an executor job to load the file contents as the trace uses a blocking file open / read call.
        myConfigDir: str = "%s/custom_components/%s" % (hass.config.config_dir, DOMAIN)
        myManifestPath: str = "%s/manifest.json" % (myConfigDir)
        myManifest: dict = await hass.async_add_executor_job(
            _getManifestFile,
            myManifestPath,
            "Integration Manifest File (%s)" % myManifestPath,
        )
        healthInfo["integration_version"] = myManifest.get("version", "unknown")

        # add client configuration data.
        clientConfig: str = ""
        if len(hass.data[DOMAIN]) > 0:
            clientConfig = str("%d: " % len(hass.data[DOMAIN]))
            data: InstanceDataSpotify = None
            for data in hass.data[DOMAIN].values():
                _logsi.LogDictionary(
                    SILevel.Verbose,
                    "InstanceDataSpotify data",
                    data,
                    prettyPrint=True,
                )
                if data.spotifyClient != None:
                    if data.spotifyClient.UserProfile != None:
                        clientConfig = clientConfig + "%s (%s), " % (
                            data.spotifyClient.UserProfile.DisplayName,
                            data.spotifyClient.UserProfile.Product,
                        )
            clientConfig = clientConfig[: len(clientConfig) - 2]  # drop ending ", "
        else:
            clientConfig = "(None Defined)"
        healthInfo["clients_configured"] = clientConfig

        # check if Spotify Web API endpoint is reachable.
        healthInfo["api_endpoint_reachable"] = system_health.async_check_can_reach_url(
            hass, "https://api.spotify.com"
        )

        # trace.
        _logsi.LogDictionary(SILevel.Verbose, "System Health results", healthInfo)

        # return system health data.
        return healthInfo

    except Exception as ex:
        # trace.
        _logsi.LogException(
            "system_health_info exception: %s" % str(ex), ex, logToSystemLogger=False
        )
        raise

    finally:
        # trace.
        _logsi.LeaveMethod(SILevel.Debug)


def _getManifestFile(filePath: str, title: str) -> str:
    """Loads the contents of the specified text file and returns them.

    Args:
        filePath (str):
            Fully-qualified file path to log.
        title (str):
            Title to assign to the log entry.

    """
    try:
        # trace.
        _logsi.EnterMethod(SILevel.Debug)
        _logsi.LogTextFile(SILevel.Verbose, title, filePath)

        # open file and read the contents.
        with open(filePath) as reader:
            data = reader.read()

        # return contents to caller.
        return json.loads(data)

    except Exception as ex:
        # trace.
        _logsi.LogException(
            "system_health_info _getManifestFile exception: %s" % str(ex),
            ex,
            logToSystemLogger=False,
        )
        return {}

    finally:
        # trace.
        _logsi.LeaveMethod(SILevel.Debug)

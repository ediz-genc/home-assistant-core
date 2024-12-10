# noqa: ignore=all

# external package imports.
# none

# our package imports.
# none


"""Spotify Integration - Application Messages - `appmessages.py`.

This module provides a strongly-typed resource class, `STAppMessages`, for managing localized and structured application
messages used throughout the Spotify integration. The class ensures consistent and thread-safe access to predefined message
strings, supporting logging, debugging, and error handling.

Key Features:
- Predefined message templates for:
  - Argument validation.
  - Service call handling and parameter checks.
  - Service execution tracking.
  - Debugging Spotify Web API queries.
  - Exception handling during service requests.
- Designed to ensure clear and localized logging and debugging messages.
- Fully thread-safe to support concurrent operations in the Home Assistant environment.

Usage:
Each message is defined as a class variable (constant) with a descriptive template string. These messages can be formatted
 dynamically with specific arguments during runtime to provide contextual information.

Examples:
- Logging missing service parameters:
  ```python
  _LOGGER.error(STAppMessages.MSG_SERVICE_ARGUMENT_NULL, "parameter_name", "service_name")

"""


class STAppMessages:
    """A strongly-typed resource class, for looking up localized strings, etc.
    Threadsafety:
        This class is fully thread-safe.
    """  # noqa: D205

    MSG_SERVICE_ARGUMENT_NULL: str = (
        "The '%s' service parameter was not specified for the '%s' service call"
    )
    """
    The '%s' service parameter was not specified for the '%s' service call
    """

    MSG_ARGUMENT_NULL: str = "The '%s' argument was not specified for the '%s' function"
    """
    The '%s' argument was not specified for the '%s' function
    """

    MSG_SERVICE_CALL_START: str = "Processing service call '%s' in async '%s' method"
    """
    Processing service call '%s' in async '%s' method
    """

    MSG_SERVICE_CALL_PARM: str = "ServiceCall Parameters"
    """
    ServiceCall Parameters
    """

    MSG_SERVICE_CALL_DATA: str = "ServiceCall Data"
    """
    ServiceCall Data
    """

    MSG_SERVICE_REQUEST_REGISTER: str = (
        "Component async_setup is registering async service: '%s'"
    )
    """
    Component async_setup is registering component async service request: '%s'
    """

    MSG_SERVICE_REQUEST_UNKNOWN: str = (
        "Service request '%s' was not recognized by the '%s' method"
    )
    """
    Service request '%s' was not recognized by the '%s' method
    """

    MSG_SERVICE_REQUEST_EXCEPTION: str = (
        "An unhandled exception occurred in Service request method '%s'; exception: %s"
    )
    """
    Service request '%s' was not recognized by the '%s' method
    """

    MSG_SERVICE_EXECUTE: str = "Executing '%s' service on media player '%s'"
    """
    Executing '%s' service on media player '%s'
    """

    MSG_SERVICE_QUERY_WEB_API: str = "Retrieving information from the Spotify Web API"
    """
    Retrieving information from the Spotify Web API
    """

    MSG_MEDIAPLAYER_SERVICE: str = "'%s': MediaPlayer is executing service '%s'"
    """
    '%s': MediaPlayer is executing service '%s'
    """

    MSG_MEDIAPLAYER_SERVICE_WITH_PARMS: str = (
        "'%s': MediaPlayer is executing service '%s' - parameters: %s"
    )
    """
    '%s': MediaPlayer is executing service '%s' - parameters: %s
    """

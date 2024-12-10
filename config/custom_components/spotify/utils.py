# noqa: ignore=all


"""Utility Functions for Spotify Integration - `utils.py`.

This module provides utility functions for the Spotify integration in Home Assistant. These functions offer common
operations such as masking sensitive information, validating delay values, and converting time positions, which
are used throughout the integration.

Key Features:
- **Password Masking**:
  - `passwordMaskDictionary`: Masks password-related fields in dictionaries to prevent sensitive information
  from being logged or displayed.
  - `passwordMaskString`: Masks the contents of a string when it contains sensitive data.
- **Delay Validation**:
  - `validateDelay`: Ensures delay values are within acceptable bounds, providing default values and maximum
  limits when necessary.
- **Time Position Conversion**:
  - `positionHMS_fromMilliSeconds`: Converts milliseconds to a `H:MM:SS` string format.
  - `positionHMS_fromSeconds`: Converts seconds to a `H:MM:SS` string format.

Functions:
1. `passwordMaskDictionary(inputObj: dict) -> dict`:
   - Masks all keys containing "password" in a given dictionary.
2. `passwordMaskString(inputObj: str) -> str`:
   - Masks the entire content of a given string, replacing it with asterisks.
3. `validateDelay(delay: float, default: float = 0.5, maxDelay: float = 10) -> float`:
   - Validates and adjusts a delay value to ensure it is non-negative and within the allowed maximum.
4. `positionHMS_fromMilliSeconds(position: int) -> str`:
   - Converts a position in milliseconds to `H:MM:SS` format.
5. `positionHMS_fromSeconds(position: int) -> str`:
   - Converts a position in seconds to `H:MM:SS` format.

Usage:
These utility functions are used across multiple components in the integration to handle sensitive data securely,
validate user input, and format time values for display.

Notes:
- The masking functions are designed to prevent accidental logging of sensitive information, such as passwords,
in trace files or logs.
- Time conversion functions ensure consistent formatting of playback positions for user interfaces.
- `validateDelay` provides robust handling of invalid or out-of-range delay values.

"""


# # get smartinspect logger reference; create a new session for this module name.
# from smartinspectpython.siauto import SIAuto, SILevel, SISession, SIColors
# import logging
# _logsi:SISession = SIAuto.Si.GetSession(__name__)
# if (_logsi == None):
#     _logsi = SIAuto.Si.AddSession(__name__, True)
# _logsi.SystemLogger = logging.getLogger(__name__)


def passwordMaskDictionary(inputObj: dict) -> dict:
    """Checks keys in a dictionary any keys that contain `password` and masks the
    value so that the password is not displayed in a trace file.

    Args:
        inputObj (dict):
            Dictionary object to check.

    Returns:
        A copy of the `inputObj` source dictionary with passwor(s) masked.

    Note that this method performs a simple copy of the dictionary.

    """
    # if input is null then don't bother.
    if inputObj is None:
        return inputObj

    # create a new dictionary.
    result: dict = {}

    # process keys in the dictionary.
    key: str
    for key in inputObj:
        keyLower: str = key.lower()
        if keyLower.find("password") == -1:
            result[key] = inputObj[key]
        else:
            value: str = inputObj[key]
            if (value is not None) and (isinstance(value, str)):
                result[key] = "".ljust(len(value), "*")

    return result


def passwordMaskString(inputObj: str) -> str:
    """Checks a string for a password value and masks the value so that the password is not displayed
    in a trace file.

    Args:
        inputObj (str):
            String object to check.

    Returns:
        A copy of the `inputObj` value with password masked.

    """
    # if input is null then don't bother.
    if inputObj is None:
        return inputObj

    # create a new value.
    result: str = "".ljust(len(inputObj), "*")

    return result


def validateDelay(delay: float, default: float = 0.5, maxDelay: float = 10) -> float:
    """Validates a delay value.

    Args:
        delay (int):
            The delay value to validate.
        default (int):
            The default delay value to set if the user-input delay is not valid.
        maxDelay (int):
            The maximum delay value allowed.
            Default is 10.

    """
    if isinstance(delay, int):
        delay = float(delay)

    if (not isinstance(delay, float)) or (delay < 0):
        result = default
    elif delay > maxDelay:
        result = maxDelay
    else:
        result = delay

    return result


def positionHMS_fromMilliSeconds(
    position: int,
) -> float:
    """Converts an integer position value from milliseconds to a string value in H:MM:SS format.

    Args:
        position (int):
            The position value (as specified in milliseconds) to convert.

    """
    result: str = "0:00:00"

    # validations.
    if isinstance(position, float):
        position = int(position)
    if (position is None) or (not isinstance(position, int)) or (position < 1):
        return result

    # convert milliseconds to H:MM:SS string format.
    nSeconds = position / 1000
    mm, ss = divmod(nSeconds, 60)  # get minutes and seconds first
    hh, mm = divmod(mm, 60)  # get hours next
    result = "%d:%02d:%02d" % (hh, mm, ss)  # format to hh:mm:ss

    # return result to caller.
    return result


def positionHMS_fromSeconds(
    position: int,
) -> float:
    """Converts an integer position value from seconds to a string value in H:MM:SS format.

    Args:
        position (int):
            The position value (as specified in seconds) to convert.

    """
    result: str = "0:00:00"

    # validations.
    if isinstance(position, float):
        position = int(position)
    if (position is None) or (position < 1):
        return result

    # convert seconds to H:MM:SS string format.
    nSeconds = int(position)
    mm, ss = divmod(nSeconds, 60)  # get minutes and seconds first
    hh, mm = divmod(mm, 60)  # get hours next
    result = "%d:%02d:%02d" % (hh, mm, ss)  # format to hh:mm:ss

    # return result to caller.
    return result

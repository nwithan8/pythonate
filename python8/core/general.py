from typing import Any, Optional


def is_none_or_empty(value) -> bool:
    return value is None or value == ""


def set_default_if_none_or_empty(value, default) -> Any:
    if is_none_or_empty(value):
        return default
    return value


def extract_boolean(value) -> bool:
    if isinstance(value, bool):
        return value
    if value.lower() in ["true", "t", "yes", "y", "enable", "en", "on", "1"]:
        return True
    elif value.lower() in ["false", "f", "no", "n", "disable", "dis", "off", "0"]:
        return False
    else:
        raise ValueError("Not a boolean: {}".format(value))

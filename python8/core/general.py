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

def is_positive_int(n):
    return n.isdigit()


def convert_string_to_bool(bool_string: str) -> bool:
    """
    Careful: True or False is valid. Check if is None to see if this conversion failed
    """
    bool_string = bool_string.strip()
    if bool_string in ['true', 'yes', 'on', 'enable']:
        return True
    elif bool_string in ['false', 'no', 'off', 'disable']:
        return False

    raise ValueError(f"Invalid bool string: {bool_string}")


def convert_bool_to_string(bool_value: bool) -> str:
    if bool_value:
        return "True"
    else:
        return "False"


def convert_bool_to_int(bool_value: bool) -> int:
    if bool_value:
        return 1
    else:
        return 0


def convert_int_to_bool(int_value: int) -> bool:
    if int_value == 1:
        return True
    elif int_value == 0:
        return False

    raise ValueError(f"Invalid int value for bool: {int_value}")


def convert_string_list_to_string(string_list: list[str]) -> str:
    return ",".join(string_list)


def convert_string_to_string_list(string: str) -> list[str]:
    return string.split(",")


def object_to_string_representation(obj: object) -> str:
    """
    Convert an object to a string

    :param obj:
    :return: String representation of the object
    """
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return str(obj)
    elif isinstance(obj, float):
        return str(obj)
    elif isinstance(obj, bool):
        return convert_bool_to_string(bool_value=obj)
    elif isinstance(obj, list):
        string_list = [object_to_string_representation(obj=o) for o in obj]
        return convert_string_list_to_string(string_list=string_list)

    raise ValueError(f'Cannot convert type {type(object)} to string representation')

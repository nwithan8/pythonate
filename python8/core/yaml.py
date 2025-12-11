import yaml


def load_from_file(file_path: str) -> dict:
    """
    Load a YAML file into a Python dictionary.

    :param file_path: Path to the YAML file
    :type file_path: str
    :return: Dictionary representation of the YAML file
    :rtype: dict
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def object_to_yaml_string(obj: object, sort_keys: bool = False) -> str:
    """
    Convert an object to a YAML string.

    :param obj: Object to convert
    :type obj: object
    :param sort_keys: (Optional) whether to sort the keys in the YAML output
    :type sort_keys: bool, optional
    :return: YAML string representation of the object
    :rtype: str
    """
    return yaml.dump(obj, default_flow_style=False, sort_keys=sort_keys)

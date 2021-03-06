import json
from typing import List, Union, Tuple


# Dictionaries #
def dict_to_json(dictionary: dict) -> json:
    """
    Convert a dictionary to valid JSON
    :param dictionary: Dictionary to convert
    :return: JSON representation of dictionary
    """
    return json.dumps(dictionary)


def combine_dictionaries(old_dictionary: dict, new_dictionary: dict, add_new_items: bool = False) -> dict:
    """
    Build a complete dictionary, overwriting values in old dictionary with values in new dictionary
    :param old_dictionary: Original (base) dictionary
    :param new_dictionary: New (updated values) dictionary
    :param add_new_items: If a new item is found in the new dictionary that is not present in the old dictionary,
    include it in the final dictionary. Otherwise, ignore it. (Default: False)
    :return: A dictionary
    """
    for k, v in new_dictionary.items():
        if k in old_dictionary.keys() or add_new_items:
            old_dictionary[k] = v
    return old_dictionary


def dictionary_is_complete(check_dictionary: dict, template_dictionary: dict, ignore_keys: List = []) -> bool:
    """
    Check that all keys in the template dictionary are present in the check_dictionary
    :param check_dictionary: Dictionary to parse
    :param template_dictionary: Dictionary to use for verification
    :param ignore_keys: List of keys to ignore when checking (Optional)
    :return: True if valid, False if not valid
    """
    for k in template_dictionary.keys():
        if k in ignore_keys or k in check_dictionary.keys():
            pass
        else:
            return False
    return True

import json
from typing import List

import sqlitedict


def dict_to_json(dictionary: dict) -> json:
    """
    Convert a dictionary to valid JSON
    :param dictionary: Dictionary to convert
    :return: JSON representation of dictionary
    """
    return json.dumps(dictionary)


def json_to_dict(json_string: str) -> dict:
    """
    Convert a JSON string to a dictionary
    :param json_string: JSON string to convert
    :return: Dictionary representation of JSON string
    """
    return json.loads(json_string)


def load_dict_from_file(file_path: str) -> dict:
    """
    Load a dictionary from a JSON file
    :param file_path: Path to JSON file
    :return: Dictionary
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_dict_to_file(dictionary: dict, file_path: str) -> None:
    """
    Save a dictionary to a JSON file
    :param dictionary: Dictionary to save
    :param file_path: Path to file
    :return: None
    """
    with open(file_path, 'w') as f:
        json.dump(dictionary, f)


def load_dict_from_sqlite(file_path: str) -> dict:
    """
    Load a dictionary from a SQLite database
    :param file_path: Path to file
    :return: Dictionary
    """
    data = {}
    with sqlitedict.SqliteDict(file_path, autocommit=True) as db:
        # copy the data from the sqlite database to the dictionary
        for k, v in db.items():
            data[k] = v
        db.close()
    return data


def save_dict_to_sqlite(dictionary: dict, file_path: str) -> None:
    """
    Save a dictionary to a SQLite database
    :param dictionary: Dictionary to save
    :param file_path: Path to file
    :return: None
    """
    with sqlitedict.SqliteDict(file_path) as db:
        # copy the data from the dictionary to the sqlite database
        for k, v in dictionary.items():
            db[k] = v
        db.commit()
        db.close()


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

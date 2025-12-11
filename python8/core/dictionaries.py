import json
from typing import List


def load_dict_from_json(json_string: str) -> dict:
    """
    Convert a JSON string into a Python dictionary.

    :param json_string: JSON string to load
    :type json_string: str
    :return: Dictionary representation of the JSON string
    :rtype: dict
    """
    return json.loads(json_string)


def load_dict_from_file(file_path: str) -> dict:
    """
    Convert a JSON file into a Python dictionary.

    :param file_path: Path to the JSON file
    :type file_path: str
    :return: Dictionary representation of the JSON file
    :rtype: dict
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_dict_from_sqlite(file_path: str) -> dict:
    """
    Load a dictionary from a SQLite database

    :param file_path: Path to file
    :type file_path: str
    :return: Dictionary
    :rtype: dict
    """
    import sqlitedict
    data = {}
    with sqlitedict.SqliteDict(file_path, autocommit=True) as db:
        # copy the data from the sqlite database to the dictionary
        for k, v in db.items():
            data[k] = v
        db.close()
    return data


def load_json_from_sqlite(file_path: str) -> str:
    """
    Load JSON data from a SQLite database

    :param file_path: Path to the database
    :type file_path: str
    :return: The JSON data
    :rtype: dict
    """
    data: dict = load_dict_from_sqlite(file_path=file_path)
    return json.dumps(data)


def save_dict_to_file(file_path: str, dictionary: dict) -> None:
    """
    Save a dictionary to a file

    :param dictionary: Dictionary to save
    :type dictionary: dict
    :param file_path: Path to file
    :type file_path: str
    :return: None
    :rtype: None
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, indent=4)


def save_json_to_file(file_path: str, data: str) -> None:
    """
    Save a JSON string to a file

    :param file_path: Path to the file
    :type file_path: str
    :param data: The JSON data
    :type data: str
    :return: None
    :rtype: None
    """
    data: dict = load_dict_from_json(json_string=data)
    save_dict_to_file(dictionary=data, file_path=file_path)


def save_dict_to_sqlite(file_path: str, dictionary: dict) -> None:
    """
    Save a dictionary to a SQLite database

    :param dictionary: Dictionary to save
    :type dictionary: dict
    :param file_path: Path to file
    :type file_path: str
    :return: None
    :rtype: None
    """
    import sqlitedict
    with sqlitedict.SqliteDict(file_path) as db:
        # copy the data from the dictionary to the sqlite database
        for k, v in dictionary.items():
            db[k] = v
        db.commit()
        db.close()


def save_json_to_sqlite(file_path: str, data: str) -> None:
    """
    Save a JSON string to a SQLite database

    :param file_path: Path to the database
    :type file_path: str
    :param data: The JSON data
    :type data: str
    :return: None
    :rtype: None
    """
    data: dict = load_dict_from_json(json_string=data)
    save_dict_to_sqlite(dictionary=data, file_path=file_path)


def object_to_json_string(obj: object) -> str:
    """
    Convert an object to a JSON string

    :param obj: Object to convert
    :type obj: object
    :return: JSON string representation of the object
    :rtype: str
    """
    return json.dumps(obj, indent=4)


def pretty_print(data: dict, sort: bool = False) -> str:
    """
    Return a pretty printed dictionary or JSON string

    :param data: data to pretty print
    :type data: dict
    :param sort: (Optional) sort the keys in the JSON data
    :type sort: bool, optional
    :return: pretty printed JSON string
    :rtype: str
    """
    return json.dumps(data, indent=4, sort_keys=sort)


def combine_dictionaries(old_dictionary: dict, new_dictionary: dict, add_new_items: bool = False) -> dict:
    """
    Build a complete dictionary, overwriting values in old dictionary with values in new dictionary

    :param old_dictionary: Original (base) dictionary
    :type old_dictionary: dict
    :param new_dictionary: New (updated values) dictionary
    :type new_dictionary: dict
    :param add_new_items: If a new item is found in the new dictionary that is not present in the old dictionary,
    include it in the final dictionary. Otherwise, ignore it. (Default: False)
    :type add_new_items: bool
    :return: A dictionary
    :rtype: dict
    """
    for k, v in new_dictionary.items():
        if k in old_dictionary.keys() or add_new_items:
            old_dictionary[k] = v
    return old_dictionary


def dictionary_is_complete(check_dictionary: dict, template_dictionary: dict, ignore_keys: List = None) -> bool:
    """
    Check that all keys in the template dictionary are present in the check_dictionary

    :param check_dictionary: Dictionary to parse
    :type check_dictionary: dict
    :param template_dictionary: Dictionary to use for verification
    :type template_dictionary: dict
    :param ignore_keys: List of keys to ignore when checking (Optional)
    :type ignore_keys: List, optional
    :return: True if valid, False if not valid
    :rtype: bool
    """
    ignore_keys = ignore_keys or []

    for k in template_dictionary.keys():
        if k in ignore_keys or k in check_dictionary.keys():
            pass
        else:
            return False
    return True

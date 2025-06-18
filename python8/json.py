from python8.dictionaries import dict_to_json, json_to_dict, load_dict_from_file, save_dict_to_file, \
    load_dict_from_sqlite, save_dict_to_sqlite


def load_json_from_file(file_path: str) -> str:
    """
    Load JSON from a file
    :param file_path: Path to the file
    :type file_path: str
    :return: The JSON data
    :rtype: str
    """
    data: dict = load_dict_from_file(file_path=file_path)
    return dict_to_json(dictionary=data)


def save_json_to_file(file_path: str, data: str) -> None:
    """
    Save JSON to a file
    :param file_path: Path to the file
    :type file_path: str
    :param data: The JSON data
    :type data: str
    :return: None
    :rtype: None
    """
    data: dict = json_to_dict(json_string=data)
    save_dict_to_file(dictionary=data, file_path=file_path)


def load_json_from_sqlite(file_path: str) -> str:
    """
    Load JSON from a SQLite database
    :param file_path: Path to the database
    :type file_path: str
    :return: The JSON data
    :rtype: dict
    """
    data: dict = load_dict_from_sqlite(file_path=file_path)
    return dict_to_json(dictionary=data)


def save_json_to_sqlite(file_path: str, data: str) -> None:
    """
    Save JSON to a SQLite database
    :param file_path: Path to the database
    :type file_path: str
    :param data: The JSON data
    :type data: str
    :return: None
    :rtype: None
    """
    data: dict = json_to_dict(json_string=data)
    save_dict_to_sqlite(dictionary=data, file_path=file_path)

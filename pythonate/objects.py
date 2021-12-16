import pickle
from typing import Union


def object_to_pickle(obj: object) -> Union[bytes, None]:
    """
    Pickle an object and return the pickled bytes.
    :param obj: The object to pickle.
    :return: Pickled object.
    """
    try:
        return pickle.dumps(obj)
    except pickle.PicklingError:
        return None


def object_to_pickle_file(obj: object, file_path: str) -> None:
    """
    Pickle an object and write it to a file.
    :param obj: The object to pickle.
    :param file_path: The file path to write the pickled object to.
    :return: None
    """
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
    except pickle.PicklingError:
        pass


def pickle_to_object(pickled_obj: bytes) -> Union[object, None]:
    """
    Unpickle an object from the pickled bytes.
    :param pickled_obj: The pickled object.
    :return: Unpickled object.
    """
    try:
        return pickle.loads(pickled_obj)
    except pickle.UnpicklingError:
        return None


def pickle_file_to_object(file_path: str) -> Union[object, None]:
    """
    Unpickle an object from a file.
    :param file_path: The file path to read the pickled object from.
    :return: Unpickled object.
    """
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except pickle.UnpicklingError:
        return None

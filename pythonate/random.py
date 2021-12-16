import random
from typing import List, Union

from pythonate.checks import object_has_attribute


def random_choice(items: List):
    """
    Get a random item from a list
    :param items: list of items
    :return: random item
    """
    return random.choice(items)


def random_with_attributes(items: List, attributes: List[str], attempts: int = 10) -> Union[object, None]:
    """
    Pick a random object with given attribute from a list
    Returns None after X failed attempts
    :param items: List of objects
    :param attributes: List of attributes to check for
    :param attempts: How many times to retry before returning None
    :return: Either a matching random object or None
    """
    if attempts == 0:
        return None
    temp_choice = random_choice(items)
    for attribute in attributes:
        if not object_has_attribute(temp_choice, attribute_name=attribute):
            return random_with_attributes(items=items, attributes=attributes, attempts=attempts - 1)
    return temp_choice

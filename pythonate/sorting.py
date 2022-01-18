import collections
import random
from typing import List, Tuple

from pythonate.checks import object_has_attribute


def shuffle(items: List) -> bool:
    """
    Randomize the order of the items in a list in-place
    :param items: list of items to shuffle
    :type items: List
    :return: True if successful, False if unsuccessful
    :rtype: bool
    """
    try:
        random.shuffle(items)
        return True
    except:
        pass
    return False


def rotate_items(items: List, shift_index: int = None) -> List:
    """
    Rotate items in a list by a specific number of steps
    :param items: list of items
    :type items: List
    :param shift_index: Optional index to shift list by. Otherwise random
    :type shift_index: int
    :return: rotated list of items
    :rtype: List
    """
    if not shift_index:
        shift_index = random.randint(0, len(items) - 1)
    collection_list = collections.deque(items)
    collection_list.rotate(shift_index)
    return list(collection_list)


def remove_duplicates(items: List) -> List:
    """
    Remove duplicate items from a list
    "Duplicate" objects must be exactly the same (all attributes)
    :param items: list of items to parse
    :type items: List
    :return: list of filtered items
    :rtype: List
    """
    return list(set(items))


def remove_duplicates_by_attribute(items: List, attribute_name: str) -> List:
    """
    Remove duplicate items from a list, comparing on a specific attribute
    :param items: list of items to parse
    :type items: List
    :param attribute_name: name of attribute to check by
    :type attribute_name: str
    :return: list of filtered items
    :rtype: List
    """
    filtered = []
    filtered_attr = []
    for item in items:
        attr = getattr(item, attribute_name)
        if attr not in filtered_attr:
            filtered.append(item)
            filtered_attr.append(attr)
    return filtered


def separate_with_and_without(items: List, attribute_name: str) -> Tuple[List, List]:
    """
    Split a list of items into those with a specific attribute and those without
    :param items: List of items
    :type items: List
    :param attribute_name: Name of attribute to look for
    :type attribute_name: str
    :return: list_with, list_without
    :rtype: Tuple[List, List]
    """
    items_with = []
    items_without = []
    for item in items:
        if object_has_attribute(obj=item, attribute_name=attribute_name):
            items_with.append(item)
        else:
            items_without.append(item)
    return items_with, items_without

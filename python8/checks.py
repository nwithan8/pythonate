def object_has_attribute(obj: object, attribute_name: str) -> bool:
    """
    Check if an object has an attribute (exists and is not None)
    :param obj: object to check
    :type obj: object
    :param attribute_name: name of attribute to find
    :type attribute_name: str
    :return: True if exists and is not None, False otherwise
    :rtype: bool
    """
    if hasattr(obj, attribute_name):
        if getattr(obj, attribute_name) is not None:
            return True
    return False

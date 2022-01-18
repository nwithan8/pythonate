def make_enums(name: str, **enums):
    """
    Creates an enum class with the given name and the given values.
    :param name: The name of the enum class.
    :type name: str
    :param enums: The values of the enum class.
    :type enums: dict
    :return: The enum class.
    :rtype: type
    """
    return type(name, (), enums)

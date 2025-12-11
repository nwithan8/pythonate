from typing import Any, Union, List


class Option:
    """
    An option is a name-value pair with a list of aliases.
    """

    def __init__(self, name: str, value: Any, aliases: List[str] = None):
        """
        :param name: The name of the option.
        :type name: str
        :param value: The value of the option.
        :type value: Any
        :param aliases: A list of aliases for the option.
        :type aliases: List[str]
        """
        self.name = name
        self.value = value
        self.aliases = aliases or []


class Options:
    """
    A collection of options.
    """

    def __init__(self, options: List[Option]):
        """
        :param options: A list of options.
        :type options: List[Option]
        """
        self.options = options

    def match(self, name: str) -> Union[Option, None]:
        """
        :param name: The name or alias of an option.
        :type name: str
        :return: The option matching the provided name or alias, or None.
        :rtype: Option | None
        """
        for option in self.options:
            if name == option.name or name in option.aliases:
                return option
        return None

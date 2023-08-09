class MissingSupportError(ImportError):
    """
    Error raised when a module is missing support for a feature
    """

    def __init__(self, extension: str):
        """
        :param extension: The extension that is missing support
        """
        super().__init__(f'This function is unavailable without the "{extension}" extension.')

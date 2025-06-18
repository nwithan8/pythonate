from enum import Enum


class Unit(Enum):
    """
    Enum for digital storage units.
    """
    BYTES = ('B', 0, 1024)
    KILOBYTES = ('KB', 1, 1024 ** 2)
    MEGABYTES = ('MB', 2, 1024 ** 3)
    GIGABYTES = ('GB', 3, 1024 ** 4)
    TERABYTES = ('TB', 4, 1024 ** 5)
    PETABYTES = ('PB', 5, 1024 ** 6)
    EXABYTES = ('EB', 6, 1024 ** 7)
    ZETTABYTES = ('ZB', 7, 1024 ** 8)
    YOTTABYTES = ('YB', 8, 1024 ** 9)


def _to_bytes(size: float, units: Unit) -> float:
    mult = float(1024)
    if units == Unit.BYTES:
        return size
    else:
        return float(size * (mult ** units.value[1]))


def _bytes_to_other(size: float, units: Unit):
    mult = float(1024)
    if units == Unit.BYTES:
        return size
    else:
        return float(size / (mult ** units.value[1]))


def simplify(size: float, units: Unit) -> 'Storage':
    """
    Simplifies a given size to the smallest unit.
    :param size: The current size.
    :type size: float
    :param units: The unit of the current size.
    :type units: Unit
    :return: A Storage object with the simplified size.
    :rtype: Storage
    """
    size_in_bytes = _to_bytes(size=size, units=units)

    if size_in_bytes < Unit.BYTES.value[2]:
        return Storage(size_in_bytes, Unit.BYTES)
    elif size_in_bytes < Unit.KILOBYTES.value[2]:
        return Storage(size_in_bytes / Unit.BYTES.value[2], Unit.KILOBYTES)
    elif size_in_bytes < Unit.MEGABYTES.value[2]:
        return Storage(size_in_bytes / Unit.KILOBYTES.value[2], Unit.MEGABYTES)
    elif size_in_bytes < Unit.GIGABYTES.value[2]:
        return Storage(size_in_bytes / Unit.MEGABYTES.value[2], Unit.GIGABYTES)
    elif size_in_bytes < Unit.TERABYTES.value[2]:
        return Storage(size_in_bytes / Unit.GIGABYTES.value[2], Unit.TERABYTES)
    elif size_in_bytes < Unit.PETABYTES.value[2]:
        return Storage(size_in_bytes / Unit.TERABYTES.value[2], Unit.PETABYTES)
    elif size_in_bytes < Unit.EXABYTES.value[2]:
        return Storage(size_in_bytes / Unit.PETABYTES.value[2], Unit.EXABYTES)
    elif size_in_bytes < Unit.ZETTABYTES.value[2]:
        return Storage(size_in_bytes / Unit.EXABYTES.value[2], Unit.ZETTABYTES)
    else:
        return Storage(size_in_bytes / Unit.ZETTABYTES.value[2], Unit.YOTTABYTES)


def to_other_unit(size: float, current_units: Unit, target_units: Unit) -> 'Storage':
    """
    Converts a given size to another unit.
    :param size: The current size.
    :type size: float
    :param current_units: The unit of the current size.
    :type current_units: Unit
    :param target_units: The unit to convert to.
    :type current_units: Unit
    :return: A Storage object with the converted size.
    :rtype: Storage
    """
    size_in_bytes = _to_bytes(size=size, units=current_units)
    new_size = _bytes_to_other(size=size_in_bytes, units=target_units)

    return Storage(new_size, target_units)


class Storage:
    """
    A class for handling digital storage sizes.
    """
    def __init__(self, size: float, units: Unit):
        """
        Initializes a Storage object.
        :param size: The size of the storage.
        :type size: float
        :param units: The unit of the storage.
        :type units: Unit
        """
        self._size = size
        self._units = units

    @property
    def _suffix(self):
        return self._units.value[0]

    def __str__(self):
        return f"{self._size}{self._suffix}"

    def __int__(self):
        return int(self._size)

    def __float__(self):
        return self._size

    @property
    def bytes(self) -> 'Storage':
        """
        Converts the current size to bytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.BYTES)

    @property
    def kilobytes(self) -> 'Storage':
        """
        Converts the current size to kilobytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.KILOBYTES)

    @property
    def megabytes(self) -> 'Storage':
        """
        Converts the current size to megabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.MEGABYTES)

    @property
    def gigabytes(self) -> 'Storage':
        """
        Converts the current size to gigabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.GIGABYTES)

    @property
    def terabytes(self) -> 'Storage':
        """
        Converts the current size to terabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.TERABYTES)

    @property
    def petabytes(self) -> 'Storage':
        """
        Converts the current size to petabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.PETABYTES)

    @property
    def exabytes(self) -> 'Storage':
        """
        Converts the current size to exabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.EXABYTES)

    @property
    def zettabytes(self) -> 'Storage':
        """
        Converts the current size to zettabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.ZETTABYTES)

    @property
    def yottabytes(self) -> 'Storage':
        """
        Converts the current size to yottabytes.
        :return: A Storage object with the converted size.
        :rtype: Storage
        """
        return to_other_unit(size=self._size, current_units=self._units, target_units=Unit.YOTTABYTES)

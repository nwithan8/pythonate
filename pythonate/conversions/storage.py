from pythonate.enums import enum

storage_units = enum(BYTES='B', KILOBYTES='KB', MEGABYTES='MB', GIGABYTES='GB', TERABYTES='TB', PETABYTES='PB',
                     EXABYTES='EB', ZETTABYTES='ZB', YOTTABYTES='YB')


class Units:
    BYTES = storage_units.BYTES
    KILOBYTES = storage_units.KILOBYTES
    MEGABYTES = storage_units.MEGABYTES
    GIGABYTES = storage_units.GIGABYTES
    TERABYTES = storage_units.TERABYTES
    PETABYTES = storage_units.PETABYTES
    EXABYTES = storage_units.EXABYTES
    ZETTABYTES = storage_units.ZETTABYTES
    YOTTABYTES = storage_units.YOTTABYTES


def _to_bytes(size: float, units: storage_units):
    mult = float(1024)
    if units == Units.BYTES:
        return size
    elif units == Units.KILOBYTES:
        return float(size * mult)
    elif units == Units.MEGABYTES:
        return float(size * (mult ** 2))
    elif units == Units.GIGABYTES:
        return float(size * (mult ** 3))
    elif units == Units.TERABYTES:
        return float(size * (mult ** 4))
    elif units == Units.PETABYTES:
        return float(size * (mult ** 5))
    elif units == Units.EXABYTES:
        return float(size * (mult ** 6))
    elif units == Units.ZETTABYTES:
        return float(size * (mult ** 7))
    else:
        return float(size * (mult ** 8))


def _bytes_to_other(size: float, units: storage_units):
    mult = float(1024)
    if units == Units.BYTES:
        return size
    elif units == Units.KILOBYTES:
        return float(size / mult)
    elif units == Units.MEGABYTES:
        return float(size / (mult ** 2))
    elif units == Units.GIGABYTES:
        return float(size / (mult ** 3))
    elif units == Units.TERABYTES:
        return float(size / (mult ** 4))
    elif units == Units.PETABYTES:
        return float(size / (mult ** 5))
    elif units == Units.EXABYTES:
        return float(size / (mult ** 6))
    elif units == Units.ZETTABYTES:
        return float(size / (mult ** 7))
    else:
        return float(size / (mult ** 8))


def simplify(size: float, units: storage_units):
    B = _to_bytes(size=size, units=units)

    B = float(B) * 1024
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776
    PB = float(KB ** 5)
    EB = float(KB ** 6)
    ZB = float(KB ** 7)
    YB = float(KB ** 8)

    if B < KB:
        return Storage(B, Units.BYTES)
    elif KB <= B < MB:
        return Storage(B / KB, Units.KILOBYTES)
    elif MB <= B < GB:
        return Storage(B / MB, Units.MEGABYTES)
    elif GB <= B < TB:
        return Storage(B / GB, Units.GIGABYTES)
    elif TB <= B < PB:
        return Storage(B / TB, Units.TERABYTES)
    elif PB <= B < EB:
        return Storage(B / PB, Units.PETABYTES)
    elif EB <= B < ZB:
        return Storage(B / EB, Units.EXABYTES)
    elif ZB <= B < YB:
        return Storage(B / ZB, Units.ZETTABYTES)
    elif YB <= B:
        return Storage(B / YB, Units.YOTTABYTES)


def to_other_unit(size: float, current_units: storage_units, target_units: storage_units):
    B = _to_bytes(size=size, units=current_units)
    new_size = _bytes_to_other(size=B, units=target_units)

    if target_units == Units.BYTES:
        return Storage(new_size, Units.BYTES)
    elif target_units == Units.KILOBYTES:
        return Storage(new_size, Units.KILOBYTES)
    elif target_units == Units.MEGABYTES:
        return Storage(new_size, Units.MEGABYTES)
    elif target_units == Units.GIGABYTES:
        return Storage(new_size, Units.GIGABYTES)
    elif target_units == Units.TERABYTES:
        return Storage(new_size, Units.TERABYTES)
    elif target_units == Units.PETABYTES:
        return Storage(new_size, Units.PETABYTES)
    elif target_units == Units.EXABYTES:
        return Storage(new_size, Units.EXABYTES)
    elif target_units == Units.ZETTABYTES:
        return Storage(new_size, Units.ZETTABYTES)
    else:
        return Storage(new_size, Units.YOTTABYTES)


class Storage:
    def __init__(self, size: float, units: storage_units):
        self._size = size
        self._units = units

    def __str__(self):
        return f"{self._size}{self._units}"

    def __int__(self):
        return int(self._size)

    def __float__(self):
        return self._size

    @property
    def bytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.BYTES)

    @property
    def kilobytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.KILOBYTES)

    @property
    def megabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.MEGABYTES)

    @property
    def gigabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.GIGABYTES)

    @property
    def terabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.TERABYTES)

    @property
    def petabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.PETABYTES)

    @property
    def exabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.EXABYTES)

    @property
    def zettabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.ZETTABYTES)

    @property
    def yottabytes(self):
        return to_other_unit(size=self._size, current_units=self._units, target_units=Units.YOTTABYTES)

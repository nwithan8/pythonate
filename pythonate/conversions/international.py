from enum import Enum


class MetricUnit(Enum):
    """
    Enum for metric units.
    """
    PICO = (-12, 'p')
    NANO = (-9, 'n')
    MICRO = (-6, 'μ')
    MILLI = (-3, 'm')
    CENTI = (-2, 'c')
    DECI = (-1, 'd')
    BASE = (-1, '')
    DECA = (1, 'da')
    HECTO = (2, 'h')
    KILO = (3, 'k')
    MEGA = (6, 'M')
    GIGA = (9, 'G')
    TERA = (12, 'T')


class ImperialDistanceUnit(Enum):
    """
    Enum for imperial distance units.
    """
    INCHES = 'in'
    FEET = 'ft'
    YARDS = 'yd'
    MILES = 'mi'


class ImperialVolumeUnit(Enum):
    """
    Enum for imperial volume units.
    """
    TEASPOONS = 'tsp'
    TABLESPOONS = 'Tbsp'
    FLUID_OUNCES = 'fl oz'
    GILLS = 'gill'
    CUPS = 'cups'
    PINTS = 'pints'
    QUARTS = 'qt'
    GALLONS = 'gal'


def get_metric_prefix(unit: MetricUnit) -> str:
    """
    Returns the prefix for a metric unit.
    :param unit: The unit to get the prefix for.
    :return: The prefix for the unit.
    """
    return unit.value[1]


def inches_to_meters(inches: float) -> float:
    """
    Converts inches to meters.
    :param inches: The number of inches to convert.
    :type inches: float
    :return: The number of meters.
    :rtype: float
    """
    return float(inches / 39.37007874)


def meters_to_inches(meters: float) -> float:
    """
    Converts meters to inches.
    :param meters: The number of meters to convert.
    :type meters: float
    :return: The number of inches.
    :rtype: float
    """
    return float(meters * 39.37007874)


def gallons_to_liters(gallons: float) -> float:
    """
    Converts gallons to liters.
    :param gallons: The number of gallons to convert.
    :type gallons: float
    :return: The number of liters.
    :rtype: float
    """
    return float(gallons / 0.26417205235815)


def liters_to_gallons(liters: float) -> float:
    """
    Converts liters to gallons.
    :param liters: The number of liters to convert.
    :type liters: float
    :return: The number of gallons.
    :rtype: float
    """
    return float(liters * 0.26417205235815)


def _to_metric_base(size: float, units: MetricUnit) -> float:
    """
    Converts a metric size to the base unit.
    :param size: The size to convert.
    :type size: float
    :param units: The units to convert from.
    :type units: MetricUnit
    :return: The size in the base unit.
    :rtype: float
    """
    return float(size * (10 ** units.value[0]))


def _metric_base_to_other_unit(size: float, units: MetricUnit) -> float:
    """
    Converts a metric size to another unit.
    :param size: The size to convert.
    :type size: float
    :param units: The units to convert to.
    :type units: MetricUnit
    :return: The size in the target unit.
    :rtype: float
    """
    return float(size / (10 ** units.value[0]))


def _metric_to_other_unit(metric_object, target_units: MetricUnit, use_class):
    base = _to_metric_base(size=metric_object._size, units=metric_object._units)
    new_size = _metric_base_to_other_unit(size=base, units=target_units)
    return use_class(size=new_size, units=target_units)


class Metric:
    """
    A class for handling metric measurements.
    """
    class Basic:
        """
        A class for handling basic metric measurements.
        """
        def __init__(self, size: float, units: MetricUnit, unit_abbreviation: str):
            """
            Initializes a new metric measurement.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: MetricUnit
            :param unit_abbreviation: The abbreviation of the unit.
            :type unit_abbreviation: str
            """
            self._size = size
            self._units = units
            self._unit_abbr = unit_abbreviation

        @property
        def _unit_string(self) -> str:
            """
            Returns the string representation of the unit.
            :return: The string representation of the unit.
            :rtype: str
            """
            return self._units.value[1]

        def __str__(self):
            return f"{self._size} {self._unit_string}{self._unit_abbr}"

        def __int__(self):
            return int(self._size)

        def __float__(self):
            return self._size

        def _pico(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.PICO,
                                         use_class=use_class)

        def _nano(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.NANO,
                                         use_class=use_class)

        def _micro(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.MICRO,
                                         use_class=use_class)

        def _milli(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.MILLI,
                                         use_class=use_class)

        def _centi(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.CENTI,
                                         use_class=use_class)

        def _deci(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.DECI,
                                         use_class=use_class)

        def _base(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.BASE,
                                         use_class=use_class)

        def _deca(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.DECA,
                                         use_class=use_class)

        def _hecto(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.HECTO,
                                         use_class=use_class)

        def _kilo(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.KILO,
                                         use_class=use_class)

        def _mega(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.MEGA,
                                         use_class=use_class)

        def _giga(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.GIGA,
                                         use_class=use_class)

        def _tera(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnit.TERA,
                                         use_class=use_class)

    class Distance(Basic):
        """
        A class representing a metric distance measurement.
        """
        def __init__(self, size: float, units: MetricUnit):
            """
            Initializes a new metric distance measurement.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: MetricUnit
            """
            super().__init__(size=size, units=units, unit_abbreviation='m')

        @property
        def picometers(self) -> 'Distance':
            """
            Returns the measurement in picometers.
            :return: The measurement in picometers.
            :rtype: Distance
            """
            return self._pico(use_class=Metric.Distance)

        @property
        def nanometers(self) -> 'Distance':
            """
            Returns the measurement in nanometers.
            :return: The measurement in nanometers.
            :rtype: Distance
            """
            return self._nano(use_class=Metric.Distance)

        @property
        def micrometers(self) -> 'Distance':
            """
            Returns the measurement in micrometers.
            :return: The measurement in micrometers.
            :rtype: Distance
            """
            return self._micro(use_class=Metric.Distance)

        @property
        def millimeters(self) -> 'Distance':
            """
            Returns the measurement in millimeters.
            :return: The measurement in millimeters.
            :rtype: Distance
            """
            return self._milli(use_class=Metric.Distance)

        @property
        def centimeters(self) -> 'Distance':
            """
            Returns the measurement in centimeters.
            :return: The measurement in centimeters.
            :rtype: Distance
            """
            return self._centi(use_class=Metric.Distance)

        @property
        def decimeters(self) -> 'Distance':
            """
            Returns the measurement in decimeters.
            :return: The measurement in decimeters.
            :rtype: Distance
            """
            return self._deci(use_class=Metric.Distance)

        @property
        def meters(self) -> 'Distance':
            """
            Returns the measurement in meters.
            :return: The measurement in meters.
            :rtype: Distance
            """
            return self._base(use_class=Metric.Distance)

        @property
        def decameters(self) -> 'Distance':
            """
            Returns the measurement in decameters.
            :return: The measurement in decameters.
            :rtype: Distance
            """
            return self._deca(use_class=Metric.Distance)

        @property
        def hectometers(self) -> 'Distance':
            """
            Returns the measurement in hectometers.
            :return: The measurement in hectometers.
            :rtype: Distance
            """
            return self._hecto(use_class=Metric.Distance)

        @property
        def kilometers(self) -> 'Distance':
            """
            Returns the measurement in kilometers.
            :return: The measurement in kilometers.
            :rtype: Distance
            """
            return self._kilo(use_class=Metric.Distance)

        @property
        def megameters(self) -> 'Distance':
            """
            Returns the measurement in megameters.
            :return: The measurement in megameters.
            :rtype: Distance
            """
            return self._mega(use_class=Metric.Distance)

        @property
        def gigameters(self) -> 'Distance':
            """
            Returns the measurement in gigameters.
            :return: The measurement in gigameters.
            :rtype: Distance
            """
            return self._giga(use_class=Metric.Distance)

        @property
        def terameters(self) -> 'Distance':
            """
            Returns the measurement in terameters.
            :return: The measurement in terameters.
            :rtype: Distance
            """
            return self._tera(use_class=Metric.Distance)

        @property
        def imperial(self) -> 'Imperial.Distance':
            """
            Returns the measurement in imperial units.
            :return: The measurement in imperial units.
            :rtype: Imperial.Distance
            """
            inches = meters_to_inches(float(self.meters))
            return Imperial.Distance(size=inches, units=ImperialDistanceUnit.INCHES)

    class Volume(Basic):
        """
        A class representing a metric volume measurement.
        """
        def __init__(self, size: float, units: MetricUnit):
            """
            Initializes a new metric volume measurement.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: MetricUnit
            """
            super().__init__(size=size, units=units, unit_abbreviation='l')

        @property
        def picoliters(self) -> 'Volume':
            """
            Returns the measurement in picoliters.
            :return: The measurement in picoliters.
            :rtype: Volume
            """
            return self._pico(use_class=Metric.Volume)

        @property
        def nanoliters(self) -> 'Volume':
            """
            Returns the measurement in nanoliters.
            :return: The measurement in nanoliters.
            :rtype: Volume
            """
            return self._nano(use_class=Metric.Volume)

        @property
        def microliters(self) -> 'Volume':
            """
            Returns the measurement in microliters.
            :return: The measurement in microliters.
            :rtype: Volume
            """
            return self._micro(use_class=Metric.Volume)

        @property
        def milliliters(self) -> 'Volume':
            """
            Returns the measurement in milliliters.
            :return: The measurement in milliliters.
            :rtype: Volume
            """
            return self._milli(use_class=Metric.Volume)

        @property
        def centiliters(self) -> 'Volume':
            """
            Returns the measurement in centiliters.
            :return: The measurement in centiliters.
            :rtype: Volume
            """
            return self._centi(use_class=Metric.Volume)

        @property
        def deciliters(self) -> 'Volume':
            """
            Returns the measurement in deciliters.
            :return: The measurement in deciliters.
            :rtype: Volume
            """
            return self._deci(use_class=Metric.Volume)

        @property
        def liters(self) -> 'Volume':
            """
            Returns the measurement in liters.
            :return: The measurement in liters.
            :rtype: Volume
            """
            return self._base(use_class=Metric.Volume)

        @property
        def decaliters(self) -> 'Volume':
            """
            Returns the measurement in decaliters.
            :return: The measurement in decaliters.
            :rtype: Volume
            """
            return self._deca(use_class=Metric.Volume)

        @property
        def hectoliters(self) -> 'Volume':
            """
            Returns the measurement in hectoliters.
            :return: The measurement in hectoliters.
            :rtype: Volume
            """
            return self._hecto(use_class=Metric.Volume)

        @property
        def kiloliters(self) -> 'Volume':
            """
            Returns the measurement in kiloliters.
            :return: The measurement in kiloliters.
            :rtype: Volume
            """
            return self._kilo(use_class=Metric.Volume)

        @property
        def megaliters(self) -> 'Volume':
            """
            Returns the measurement in megaliters.
            :return: The measurement in megaliters.
            :rtype: Volume
            """
            return self._mega(use_class=Metric.Volume)

        @property
        def gigaliters(self) -> 'Volume':
            """
            Returns the measurement in gigaliters.
            :return: The measurement in gigaliters.
            :rtype: Volume
            """
            return self._giga(use_class=Metric.Volume)

        @property
        def teraliters(self) -> 'Volume':
            """
            Returns the measurement in teraliters.
            :return: The measurement in teraliters.
            :rtype: Volume
            """
            return self._tera(use_class=Metric.Volume)

        @property
        def imperial(self) -> 'Imperial.Volume':
            """
            Returns the measurement in imperial units.
            :return: The measurement in imperial units.
            :rtype: Imperial.Volume
            """
            gallons = liters_to_gallons(float(self.liters))
            return Imperial.Volume(size=gallons, units=ImperialVolumeUnit.GALLONS)

        @property
        def cm3(self) -> 'Metric.Area':
            """
            Returns the measurement in cubic centimeters.
            :return: The measurement in cubic centimeters.
            :rtype: Metric.Area
            """
            num = self.milliliters._size
            return Metric.Area(size=num, units=MetricUnit.CENTI)

    class Area(Basic):
        """
        A class representing a metric area measurement.
        """
        def __init__(self, size: float, units: MetricUnit):
            super().__init__(size=size, units=units, unit_abbreviation='m^3')


class Imperial:
    """
    A class for handling imperial measurements.
    """
    class Basic:
        """
        A class for handling basic imperial measurements.
        """
        def __init__(self, size: float, units):
            """
            Initializes a new imperial measurement.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: ImperialUnit
            """
            self._size = size
            self._units = units

        @property
        def _unit_string(self) -> str:
            return self._units.value

        def __str__(self):
            return f"{self._size} {self._unit_string}"

        def __int__(self):
            return int(self._size)

        def __float__(self):
            return self._size

    class Distance(Basic):
        """
        A class representing an imperial distance measurement.
        """
        def __init__(self, size: float, units: ImperialDistanceUnit):
            """
            Initializes a new imperial distance measurement.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: ImperialDistanceUnit
            """
            super().__init__(size=size, units=units)

        def _to_inches(self, size: float, units: ImperialDistanceUnit) -> float:
            """
            Converts the measurement to inches.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: ImperialDistanceUnit
            :return: The measurement in inches.
            :rtype: float
            """
            if units == ImperialDistanceUnit.INCHES:
                return float(size)
            size = float(size * 12)
            if units == ImperialDistanceUnit.FEET:
                return size
            size = float(size * 3)
            if units == ImperialDistanceUnit.YARDS:
                return size
            size = float(size * 1760)
            return size

        def to_other_unit(self, size: float, current_units: ImperialDistanceUnit,
                          target_units: ImperialDistanceUnit) -> 'Imperial.Distance':
            """
            Converts the measurement to another unit.
            :param size: The size of the measurement.
            :type size: float
            :param current_units: The units of the measurement.
            :type current_units: ImperialDistanceUnit
            :param target_units: The units to convert to.
            :type target_units: ImperialDistanceUnit
            :return: The measurement in the target units.
            :rtype: Imperial.Distance
            """
            size = float(self._to_inches(size=size, units=current_units))

            if target_units == ImperialDistanceUnit.INCHES:
                return Imperial.Distance(size, ImperialDistanceUnit.INCHES)
            size = float(size / 12)
            if target_units == ImperialDistanceUnit.FEET:
                return Imperial.Distance(size, ImperialDistanceUnit.FEET)
            size = float(size / 3)
            if target_units == ImperialDistanceUnit.YARDS:
                return Imperial.Distance(size, ImperialDistanceUnit.YARDS)
            size = float(size / 1760)
            return Imperial.Distance(size, ImperialDistanceUnit.MILES)

        @property
        def inches(self) -> 'Imperial.Distance':
            """
            Gets the measurement in inches.
            :return: The measurement in inches.
            :rtype: Imperial.Distance
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.INCHES)

        @property
        def feet(self) -> 'Imperial.Distance':
            """
            Gets the measurement in feet.
            :return: The measurement in feet.
            :rtype: Imperial.Distance
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.FEET)

        @property
        def yards(self) -> 'Imperial.Distance':
            """
            Gets the measurement in yards.
            :return: The measurement in yards.
            :rtype: Imperial.Distance
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.YARDS)

        @property
        def miles(self) -> 'Imperial.Distance':
            """
            Gets the measurement in miles.
            :return: The measurement in miles.
            :rtype: Imperial.Distance
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.MILES)

        @property
        def metric(self) -> Metric.Distance:
            """
            Gets the measurement in metric units.
            :return: The measurement in metric units.
            :rtype: Metric.Distance
            """
            meters = inches_to_meters(float(self.inches))
            return Metric.Distance(size=meters, units=MetricUnit.BASE)

    class Volume(Basic):
        """
        A class representing an imperial volume measurement.
        """
        def __init__(self, size: float, units: ImperialVolumeUnit):
            """
            Initializes a new imperial volume measurement.
            """
            super().__init__(size=size, units=units)

        def _to_teaspoon(self, size: float, units: ImperialVolumeUnit) -> float:
            """
            Converts the measurement to teaspoons.
            :param size: The size of the measurement.
            :type size: float
            :param units: The units of the measurement.
            :type units: ImperialVolumeUnit
            :return: The measurement in teaspoons.
            :rtype: float
            """
            if units == ImperialVolumeUnit.TEASPOONS:
                return float(size)
            size = float(size * 3)
            if units == ImperialVolumeUnit.TABLESPOONS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnit.FLUID_OUNCES:
                return size
            size = float(size * 4)
            if units == ImperialVolumeUnit.GILLS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnit.CUPS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnit.PINTS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnit.QUARTS:
                return size
            size = float(size * 4)
            return size

        def to_other_unit(self, size: float, current_units: ImperialVolumeUnit,
                          target_units: ImperialVolumeUnit) -> 'Imperial.Volume':
            """
            Converts the measurement to another unit.
            :param size: The size of the measurement.
            :type size: float
            :param current_units: The current units of the measurement.
            :type current_units: ImperialVolumeUnit
            :param target_units: The target units of the measurement.
            :type target_units: ImperialVolumeUnit
            :return: The measurement in the target units.
            :rtype: Imperial.Volume
            """
            size = float(self._to_teaspoon(size=size, units=current_units))

            if target_units == ImperialVolumeUnit.TEASPOONS:
                return Imperial.Volume(size, ImperialVolumeUnit.TEASPOONS)
            size = float(size / 3)
            if target_units == ImperialVolumeUnit.TABLESPOONS:
                return Imperial.Volume(size, ImperialVolumeUnit.TABLESPOONS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnit.FLUID_OUNCES:
                return Imperial.Volume(size, ImperialVolumeUnit.FLUID_OUNCES)
            size = float(size / 4)
            if target_units == ImperialVolumeUnit.GILLS:
                return Imperial.Volume(size, ImperialVolumeUnit.GILLS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnit.CUPS:
                return Imperial.Volume(size, ImperialVolumeUnit.CUPS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnit.PINTS:
                return Imperial.Volume(size, ImperialVolumeUnit.PINTS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnit.QUARTS:
                return Imperial.Volume(size, ImperialVolumeUnit.QUARTS)
            size = float(size / 4)
            return Imperial.Volume(size, ImperialVolumeUnit.GALLONS)

        @property
        def teaspoons(self) -> 'Imperial.Volume':
            """
            Gets the measurement in teaspoons.
            :return: The measurement in teaspoons.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.TEASPOONS)

        @property
        def tablespoons(self) -> 'Imperial.Volume':
            """
            Gets the measurement in tablespoons.
            :return: The measurement in tablespoons.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.TABLESPOONS)

        @property
        def fluid_ounces(self) -> 'Imperial.Volume':
            """
            Gets the measurement in fluid ounces.
            :return: The measurement in fluid ounces.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.FLUID_OUNCES)

        @property
        def gills(self) -> 'Imperial.Volume':
            """
            Gets the measurement in gills.
            :return: The measurement in gills.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.GILLS)

        @property
        def cups(self) -> 'Imperial.Volume':
            """
            Gets the measurement in cups.
            :return: The measurement in cups.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.CUPS)

        @property
        def pints(self) -> 'Imperial.Volume':
            """
            Gets the measurement in pints.
            :return: The measurement in pints.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.PINTS)

        @property
        def quarts(self) -> 'Imperial.Volume':
            """
            Gets the measurement in quarts.
            :return: The measurement in quarts.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.QUARTS)

        @property
        def gallons(self) -> 'Imperial.Volume':
            """
            Gets the measurement in gallons.
            :return: The measurement in gallons.
            :rtype: Imperial.Volume
            """
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.GALLONS)

        @property
        def metric(self) -> Metric.Volume:
            """
            Gets the measurement in metric.
            :return: The measurement in metric.
            :rtype: Metric.Volume
            """
            liters = gallons_to_liters(float(self.gallons))
            return Metric.Volume(size=liters, units=MetricUnit.BASE)

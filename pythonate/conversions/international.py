from enum import Enum


class MetricUnit(Enum):
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
    INCHES = 'in'
    FEET = 'ft'
    YARDS = 'yd'
    MILES = 'mi'


class ImperialVolumeUnit(Enum):
    TEASPOONS = 'tsp'
    TABLESPOONS = 'Tbsp'
    FLUID_OUNCES = 'fl oz'
    GILLS = 'gill'
    CUPS = 'cups'
    PINTS = 'pints'
    QUARTS = 'qt'
    GALLONS = 'gal'


def get_metric_prefix(unit: MetricUnit):
    return unit.value[1]


def inches_to_meters(inches: float):
    return float(inches / 39.37007874)


def meters_to_inches(meters: float):
    return float(meters * 39.37007874)


def gallons_to_liters(gallons: float):
    return float(gallons / 0.26417205235815)


def liters_to_gallons(liters: float):
    return float(liters * 0.26417205235815)


def _to_metric_base(size: float, units: MetricUnit):
    return float(size * (10 ** units.value[0]))


def _metric_base_to_other_unit(size: float, units: MetricUnit):
    return float(size / (10 ** units.value[0]))


def _metric_to_other_unit(metric_object, target_units: MetricUnit, use_class):
    base = _to_metric_base(size=metric_object._size, units=metric_object._units)
    new_size = _metric_base_to_other_unit(size=base, units=target_units)
    return use_class(size=new_size, units=target_units)


class Metric:
    class Basic:
        def __init__(self, size: float, units: MetricUnit, unit_abbreviation: str):
            self._size = size
            self._units = units
            self._unit_abbr = unit_abbreviation

        @property
        def _unit_string(self) -> str:
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
        def __init__(self, size: float, units: MetricUnit):
            super().__init__(size=size, units=units, unit_abbreviation='m')

        @property
        def picometers(self):
            return self._pico(use_class=Metric.Distance)

        @property
        def nanometers(self):
            return self._nano(use_class=Metric.Distance)

        @property
        def micrometers(self):
            return self._micro(use_class=Metric.Distance)

        @property
        def millimeters(self):
            return self._milli(use_class=Metric.Distance)

        @property
        def centimeters(self):
            return self._centi(use_class=Metric.Distance)

        @property
        def decimeters(self):
            return self._deci(use_class=Metric.Distance)

        @property
        def meters(self):
            return self._base(use_class=Metric.Distance)

        @property
        def decameters(self):
            return self._deca(use_class=Metric.Distance)

        @property
        def hectometers(self):
            return self._hecto(use_class=Metric.Distance)

        @property
        def kilometers(self):
            return self._kilo(use_class=Metric.Distance)

        @property
        def megameters(self):
            return self._mega(use_class=Metric.Distance)

        @property
        def gigameters(self):
            return self._giga(use_class=Metric.Distance)

        @property
        def terameters(self):
            return self._tera(use_class=Metric.Distance)

        @property
        def imperial(self):
            inches = meters_to_inches(float(self.meters))
            return Imperial.Distance(size=inches, units=ImperialDistanceUnit.INCHES)

    class Volume(Basic):
        def __init__(self, size: float, units: MetricUnit):
            super().__init__(size=size, units=units, unit_abbreviation='l')

        @property
        def picoliters(self):
            return self._pico(use_class=Metric.Volume)

        @property
        def nanoliters(self):
            return self._nano(use_class=Metric.Volume)

        @property
        def microliters(self):
            return self._micro(use_class=Metric.Volume)

        @property
        def milliliters(self):
            return self._milli(use_class=Metric.Volume)

        @property
        def centiliters(self):
            return self._centi(use_class=Metric.Volume)

        @property
        def deciliters(self):
            return self._deci(use_class=Metric.Volume)

        @property
        def liters(self):
            return self._base(use_class=Metric.Volume)

        @property
        def decaliters(self):
            return self._deca(use_class=Metric.Volume)

        @property
        def hectoliters(self):
            return self._hecto(use_class=Metric.Volume)

        @property
        def kiloliters(self):
            return self._kilo(use_class=Metric.Volume)

        @property
        def megaliters(self):
            return self._mega(use_class=Metric.Volume)

        @property
        def gigaliters(self):
            return self._giga(use_class=Metric.Volume)

        @property
        def teraliters(self):
            return self._tera(use_class=Metric.Volume)

        @property
        def imperial(self):
            gallons = liters_to_gallons(float(self.liters))
            return Imperial.Volume(size=gallons, units=ImperialVolumeUnit.GALLONS)

        @property
        def cm3(self):
            num = self.milliliters._size
            return Metric.Area(size=num, units=MetricUnit.CENTI)

    class Area(Basic):
        def __init__(self, size: float, units: MetricUnit):
            super().__init__(size=size, units=units, unit_abbreviation='m^3')


class Imperial:
    class Basic:
        def __init__(self, size: float, units):
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
        def __init__(self, size: float, units: ImperialDistanceUnit):
            super().__init__(size=size, units=units)

        def _to_inches(self, size: float, units: ImperialDistanceUnit):
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
                          target_units: ImperialDistanceUnit):
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
        def inches(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.INCHES)

        @property
        def feet(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.FEET)

        @property
        def yards(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.YARDS)

        @property
        def miles(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnit.MILES)

        @property
        def metric(self) -> Metric.Distance:
            meters = inches_to_meters(float(self.inches))
            return Metric.Distance(size=meters, units=MetricUnit.BASE)

    class Volume(Basic):
        def __init__(self, size: float, units: ImperialVolumeUnit):
            super().__init__(size=size, units=units)

        def _to_teaspoon(self, size: float, units: ImperialVolumeUnit):
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
                          target_units: ImperialVolumeUnit):
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
        def teaspoons(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.TEASPOONS)

        @property
        def tablespoons(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.TABLESPOONS)

        @property
        def fluid_ounces(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.FLUID_OUNCES)

        @property
        def gills(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.GILLS)

        @property
        def cups(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.CUPS)

        @property
        def pints(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.PINTS)

        @property
        def quarts(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.QUARTS)

        @property
        def gallons(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnit.GALLONS)

        @property
        def metric(self) -> Metric.Volume:
            liters = gallons_to_liters(float(self.gallons))
            return Metric.Volume(size=liters, units=MetricUnit.BASE)

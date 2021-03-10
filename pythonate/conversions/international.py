from pythonate.enums import enum

imperial_distance_units = enum(INCHES='in', FEET='ft', YARDS='yd', MILES='mi')

imperial_volume_units = enum(TEASPOONS='tsp', TABLESPOONS='Tbsp',
                             FLUIDOUNCES='fl oz', GILLS='gill',
                             CUPS='cups', PINTS='pints',
                             QUARTS='qt', GALLONS='gal')
metric_units = enum(PICO=-12, NANO=-9, MICRO=-6,
                    MILLI=-3, CENTI=-2, DECI=-1,
                    BASE=0, DECA=1, HECTO=2,
                    KILO=3, MEGA=6, GIGA=9, TERA=12)
metric_prefixes = {
    -12: 'p',
    -9: 'n',
    -6: 'μ',
    -3: 'm',
    -2: 'c',
    -1: 'd',
    0: '',
    1: 'da',
    2: 'h',
    3: 'k',
    6: 'M',
    9: 'G',
    12: 'T'
}


class ImperialDistanceUnits:
    INCHES = imperial_distance_units.INCHES
    FEET = imperial_distance_units.FEET
    YARDS = imperial_distance_units.YARDS
    MILES = imperial_distance_units.MILES


class ImperialVolumeUnits:
    TEASPOONS = imperial_volume_units.TEASPOONS
    TABLESPOONS = imperial_volume_units.TABLESPOONS
    FLUIDOUNCES = imperial_volume_units.FLUIDOUNCES
    GILLS = imperial_volume_units.GILLS
    CUPS = imperial_volume_units.CUPS
    PINTS = imperial_volume_units.PINTS
    QUARTS = imperial_volume_units.QUARTS
    GALLONS = imperial_volume_units.GALLONS


class MetricUnits:
    PIC0 = metric_units.PICO
    NANO = metric_units.NANO
    MICRO = metric_units.MICRO
    MILLI = metric_units.MILLI
    CENTI = metric_units.CENTI
    DECI = metric_units.DECI
    BASE = metric_units.BASE
    DECA = metric_units.DECA
    HECTO = metric_units.HECTO
    KILO = metric_units.KILO
    MEGA = metric_units.MEGA
    GIGA = metric_units.GIGA
    TERA = metric_units.TERA


def get_metric_prefix(unit: metric_units):
    return metric_prefixes.get(unit, '')


def inches_to_meters(inches: float):
    return float(inches / 39.37007874)


def meters_to_inches(meters: float):
    return float(meters * 39.37007874)


def gallons_to_liters(gallons: float):
    return float(gallons / 0.26417205235815)


def liters_to_gallons(liters: float):
    return float(liters * 0.26417205235815)


def _to_metric_base(size: float, units: metric_units):
    return float(size * (10 ** units))


def _metric_base_to_other_unit(size: float, units: metric_units):
    return float(size / (10 ** units))


def _metric_to_other_unit(metric_object, target_units: metric_units, use_class):
    base = _to_metric_base(size=metric_object._size, units=metric_object._units)
    new_size = _metric_base_to_other_unit(size=base, units=target_units)
    return use_class(size=new_size, units=target_units)


class Metric:
    class Basic:
        def __init__(self, size: float, units: metric_units, unit_abbreviation: str):
            self._size = size
            self._units = units
            self._unit_abbr = unit_abbreviation

        def __str__(self):
            return f"{self._size} {get_metric_prefix(self._units)}{self._unit_abbr}"

        def __int__(self):
            return int(self._size)

        def __float__(self):
            return self._size

        def _pico(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.PIC0,
                                         use_class=use_class)

        def _nano(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.NANO,
                                         use_class=use_class)

        def _micro(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.MICRO,
                                         use_class=use_class)

        def _milli(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.MILLI,
                                         use_class=use_class)

        def _centi(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.CENTI,
                                         use_class=use_class)

        def _deci(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.DECI,
                                         use_class=use_class)

        def _base(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.BASE,
                                         use_class=use_class)

        def _deca(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.DECA,
                                         use_class=use_class)

        def _hecto(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.HECTO,
                                         use_class=use_class)

        def _kilo(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.KILO,
                                         use_class=use_class)

        def _mega(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.MEGA,
                                         use_class=use_class)

        def _giga(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.GIGA,
                                         use_class=use_class)

        def _tera(self, use_class):
            return _metric_to_other_unit(metric_object=self, target_units=MetricUnits.TERA,
                                         use_class=use_class)

    class Distance(Basic):
        def __init__(self, size: float, units: metric_units):
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
            return Imperial.Distance(size=inches, units=ImperialDistanceUnits.INCHES)

    class Volume(Basic):
        def __init__(self, size: float, units: metric_units):
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
            return Imperial.Volume(size=gallons, units=ImperialVolumeUnits.GALLONS)

        @property
        def cm3(self):
            return self.milliliters

    class Area(Basic):
        def __init__(self, size: float, units: metric_units):
            super().__init__(size=size, units=units, unit_abbreviation='m^3')


class Imperial:
    class Basic:
        def __init__(self, size: float, units: imperial_distance_units):
            self._size = size
            self._units = units

        def __str__(self):
            return f"{self._size} {self._units}"

        def __int__(self):
            return int(self._size)

        def __float__(self):
            return self._size

    class Distance(Basic):
        def __init__(self, size: float, units: imperial_distance_units):
            super().__init__(size=size, units=units)

        def _to_inches(self, size: float, units: imperial_distance_units):
            if units == ImperialDistanceUnits.INCHES:
                return float(size)
            size = float(size * 12)
            if units == ImperialDistanceUnits.FEET:
                return size
            size = float(size * 3)
            if units == ImperialDistanceUnits.YARDS:
                return size
            size = float(size * 1760)
            return size

        def to_other_unit(self, size: float, current_units: imperial_distance_units,
                          target_units: imperial_distance_units):
            size = float(self._to_inches(size=size, units=current_units))

            if target_units == ImperialDistanceUnits.INCHES:
                return Imperial.Distance(size, ImperialDistanceUnits.INCHES)
            size = float(size / 12)
            if target_units == ImperialDistanceUnits.FEET:
                return Imperial.Distance(size, ImperialDistanceUnits.FEET)
            size = float(size / 3)
            if target_units == ImperialDistanceUnits.YARDS:
                return Imperial.Distance(size, ImperialDistanceUnits.YARDS)
            size = float(size / 1760)
            return Imperial.Distance(size, ImperialDistanceUnits.MILES)

        @property
        def inches(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnits.INCHES)

        @property
        def feet(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnits.FEET)

        @property
        def yards(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnits.YARDS)

        @property
        def miles(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialDistanceUnits.MILES)

        @property
        def metric(self):
            meters = inches_to_meters(float(self.inches))
            return Metric.Distance(size=meters, units=MetricUnits.BASE)

    class Volume(Basic):
        def __init__(self, size: float, units: imperial_volume_units):
            super().__init__(size=size, units=units)

        def _to_teaspoon(self, size: float, units: imperial_volume_units):
            if units == ImperialVolumeUnits.TEASPOONS:
                return float(size)
            size = float(size * 3)
            if units == ImperialVolumeUnits.TABLESPOONS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnits.FLUIDOUNCES:
                return size
            size = float(size * 4)
            if units == ImperialVolumeUnits.GILLS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnits.CUPS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnits.PINTS:
                return size
            size = float(size * 2)
            if units == ImperialVolumeUnits.QUARTS:
                return size
            size = float(size * 4)
            return size

        def to_other_unit(self, size: float, current_units: imperial_volume_units,
                          target_units: imperial_volume_units):
            size = float(self._to_teaspoon(size=size, units=current_units))

            if target_units == ImperialVolumeUnits.TEASPOONS:
                return Imperial.Volume(size, ImperialVolumeUnits.TEASPOONS)
            size = float(size / 3)
            if target_units == ImperialVolumeUnits.TABLESPOONS:
                return Imperial.Volume(size, ImperialVolumeUnits.TABLESPOONS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnits.FLUIDOUNCES:
                return Imperial.Volume(size, ImperialVolumeUnits.FLUIDOUNCES)
            size = float(size / 4)
            if target_units == ImperialVolumeUnits.GILLS:
                return Imperial.Volume(size, ImperialVolumeUnits.GILLS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnits.CUPS:
                return Imperial.Volume(size, ImperialVolumeUnits.CUPS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnits.PINTS:
                return Imperial.Volume(size, ImperialVolumeUnits.PINTS)
            size = float(size / 2)
            if target_units == ImperialVolumeUnits.QUARTS:
                return Imperial.Volume(size, ImperialVolumeUnits.QUARTS)
            size = float(size / 4)
            return Imperial.Volume(size, ImperialVolumeUnits.GALLONS)

        @property
        def teaspoons(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.TEASPOONS)

        @property
        def tablespoons(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.TABLESPOONS)

        @property
        def fluid_ounces(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.FLUIDOUNCES)

        @property
        def gills(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.GILLS)

        @property
        def cups(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.CUPS)

        @property
        def pints(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.PINTS)

        @property
        def quarts(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.QUARTS)

        @property
        def gallons(self):
            return self.to_other_unit(size=self._size, current_units=self._units,
                                      target_units=ImperialVolumeUnits.GALLONS)

        @property
        def metric(self):
            liters = gallons_to_liters(float(self.gallons))
            return Metric.Volume(size=liters, units=MetricUnits.BASE)

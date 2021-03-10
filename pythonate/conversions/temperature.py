from pythonate.enums import enum

temperature_units = enum(FAHRENHEIT='F', CELSIUS='C', KELVIN='K')


class Units:
    FAHRENHEIT = temperature_units.FAHRENHEIT
    CELSIUS = temperature_units.CELSIUS
    KELVIN = temperature_units.KELVIN


def f_to_c(f: float):
    return (f - 32) * (5 / 9)


def c_to_f(c: float):
    return (c * 1.8) + 32


def c_to_k(c: float):
    return c + 273.15


def k_to_c(k: float):
    return k - 273.15


def f_to_k(f: float):
    c = f_to_c(f=f)
    return c_to_k(c=c)


def k_to_f(k: float):
    c = k_to_c(k=k)
    return c_to_f(c=c)


class Temperature:
    def __init__(self, temperature: float, units: temperature_units):
        self._temp = temperature
        self._units = units

    def __str__(self):
        return f"{self._temp}{'' if self._units == temperature_units.KELVIN else '°'}{self._units}"

    def __int__(self):
        return int(self._temp)

    def __float__(self):
        return self._temp

    @property
    def fahrenheit(self):
        if self._units == temperature_units.CELSIUS:
            return Temperature(c_to_f(c=self._temp), temperature_units.FAHRENHEIT)
        if self._units == temperature_units.KELVIN:
            return Temperature(k_to_f(k=self._temp), temperature_units.FAHRENHEIT)
        if self._units == temperature_units.FAHRENHEIT:
            return self

    @property
    def celsius(self):
        if self._units == temperature_units.CELSIUS:
            return self
        if self._units == temperature_units.KELVIN:
            return Temperature(k_to_c(k=self._temp), temperature_units.CELSIUS)
        if self._units == temperature_units.FAHRENHEIT:
            return Temperature(f_to_c(f=self._temp), temperature_units.CELSIUS)

    @property
    def kelvin(self):
        if self._units == temperature_units.CELSIUS:
            return Temperature(c_to_k(c=self._temp), temperature_units.KELVIN)
        if self._units == temperature_units.KELVIN:
            return self
        if self._units == temperature_units.FAHRENHEIT:
            return Temperature(f_to_k(f=self._temp), temperature_units.KELVIN)

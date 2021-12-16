from enum import Enum


class Unit(Enum):
    CELSIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'


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
    def __init__(self, temperature: float, units: Unit):
        self._temp = temperature
        self._units = units

    def __str__(self):
        return f"{self._temp}{'' if self._units == Unit.KELVIN else '°'}{self._units}"

    def __int__(self):
        return int(self._temp)

    def __float__(self):
        return self._temp

    @property
    def fahrenheit(self):
        if self._units == Unit.CELSIUS:
            return Temperature(c_to_f(c=self._temp), Unit.FAHRENHEIT)
        if self._units == Unit.KELVIN:
            return Temperature(k_to_f(k=self._temp), Unit.FAHRENHEIT)
        if self._units == Unit.FAHRENHEIT:
            return self

    @property
    def celsius(self):
        if self._units == Unit.CELSIUS:
            return self
        if self._units == Unit.KELVIN:
            return Temperature(k_to_c(k=self._temp), Unit.CELSIUS)
        if self._units == Unit.FAHRENHEIT:
            return Temperature(f_to_c(f=self._temp), Unit.CELSIUS)

    @property
    def kelvin(self):
        if self._units == Unit.CELSIUS:
            return Temperature(c_to_k(c=self._temp), Unit.KELVIN)
        if self._units == Unit.KELVIN:
            return self
        if self._units == Unit.FAHRENHEIT:
            return Temperature(f_to_k(f=self._temp), Unit.KELVIN)

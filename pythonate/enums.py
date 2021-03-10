from enum import Enum


def enum(**enums):
    return type('Enum', (), enums)

import os
from enum import Enum
from distutils.util import strtobool


class Attribute(Enum):
    OPTIONS = "options"
    MIN = "min_length"
    MAX = "max_length"
    START = "start_with"
    END = "end_with"
    INCLUDE = "include"
    HAS_DIGIT = "has_digit"
    HAS_SPECIAL = "has_special"
    HAS_LOWER = "has_lower"
    HAS_UPPER = "has_upper"


options_dict = {Attribute.MIN: 9,
                Attribute.MAX: 10,
                Attribute.START: 'F',
                Attribute.END: 'M',
                Attribute.INCLUDE: 'text',
                Attribute.HAS_SPECIAL: False,
                Attribute.HAS_DIGIT: True,
                Attribute.HAS_UPPER: True,
                Attribute.HAS_LOWER: True
                }


def print_options():
    for option, value in options_dict.items():
        print(f"{option.value} = {value}")


def set_min_length(min):
    options_dict[Attribute.MIN] = int(min)


def set_max_length(max):
    options_dict[Attribute.MAX] = int(max)


def set_start_with(start):
    options_dict[Attribute.START] = start


def set_end_with(end):
    options_dict[Attribute.END] = end


def set_include(include):
    options_dict[Attribute.INCLUDE] = include


def set_has_digit(has_digit):
    options_dict[Attribute.HAS_DIGIT] = strtobool(has_digit)


def set_has_special(has_special):
    options_dict[Attribute.HAS_SPECIAL] = strtobool(has_special)


def set_has_lower(has_lower):
    options_dict[Attribute.HAS_LOWER] = strtobool(has_lower)


def set_has_upper(has_upper):
    options_dict[Attribute.HAS_UPPER] = strtobool(has_upper)


def clear_screen():
    if "Windows" in os.name:
        os.system('cls')
    else:
        os.system('clear')


def execute():
    from blue_words import generate_wordlist
    generate_wordlist(options_dict)

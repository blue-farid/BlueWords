from enum import Enum


class Attribute(Enum):
    MIN = "min_length"
    MAX = "max_length"
    START = "start_with"
    END = "end_with"
    INCLUDE = "include"
    HAS_DIGIT = "has_digit"
    HAS_SPECIAL = "has_special_character"
    HAS_LOWER = "has_lower_case_character"
    HAS_UPPER = "has_upper_case_character"


options_dict = {Attribute.MIN: 5,
                Attribute.MAX: 5,
                Attribute.START: '?',
                Attribute.END: '?',
                Attribute.INCLUDE: '?'}


def print_options():
    for option, value in options_dict:
        print(f"{option} = {value}")


def set_min_length(min):
    options_dict[Attribute.MIN] = min


def set_max_length(max):
    options_dict[Attribute.MAX] = max


def set_start_with(start):
    options_dict[Attribute.START] = start


def set_end_with(end):
    options_dict[Attribute.END] = end


def set_include(include):
    options_dict[Attribute.INCLUDE] = include


def set_has_digit(has_digit):
    options_dict[Attribute.HAS_DIGIT] = has_digit


def set_has_special(has_special):
    options_dict[Attribute.HAS_SPECIAL] = has_special


def set_has_lower(has_lower):
    options_dict[Attribute.HAS_LOWER] = has_lower


def set_has_upper(has_upper):
    options_dict[Attribute.HAS_UPPER] = has_upper



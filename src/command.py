import json
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


with open('options.json') as options_file:
    options_dict = json.load(options_file)

HELP_MESSAGE = """
commands:
    - options: show options and attributes that you can set
    - set [option] [value]: assign to an option a value.
        - list of the attributes that you can set:
            - min_length: specifies the min_length of the password
                - example: set min_length 5
                
            - max_length: specifies the max_length of the password
                - example: set max_length 5
                
            - start_with: determines the beginning characters (MUST be on double-quotation sign ('"'))
                It can be null if set to "?".
                - example: set start_with "blue_farid"
            - end_with: determines the last characters (MUST be on double-quotation sign ('"'))
                It can be null if set to "?".
                - example: set end_with "blue_farid"
                
            -  include: use this when you sure the password has a specific phrase. but do not know where.
                at the beginning? at the end? the middle? (MUST be on double-quotation sign ('"'))
                It can be null if set to "?".
                - example: set include "STRONG_P@ssword"
            
            - has_special: specifies that the password contains special characters or not (True or False)
                - example: set has_special True
            
            - has_digit: specifies that the password contains digits or not (True or False)
            - has_upper: specifies that the password contains upper-case characters or not (True or False)
            - has_lower: specifies that the password contains lower-case characters or not (True or False)
    
    - clear: clear screen
    - help: prints this message
    - execute: generates the wordlist
    - exit: save and terminate the app
"""


def print_options():
    for option, value in options_dict.items():
        print(f"{option} = {value}")


def set_min_length(min):
    options_dict[Attribute.MIN.value] = int(min)


def set_max_length(max):
    options_dict[Attribute.MAX.value] = int(max)


def set_start_with(start):
    options_dict[Attribute.START.value] = start


def set_end_with(end):
    options_dict[Attribute.END.value] = end


def set_include(include):
    options_dict[Attribute.INCLUDE.value] = include


def set_has_digit(has_digit):
    options_dict[Attribute.HAS_DIGIT.value] = has_digit


def set_has_special(has_special):
    options_dict[Attribute.HAS_SPECIAL.value] = has_special


def set_has_lower(has_lower):
    options_dict[Attribute.HAS_LOWER.value] = has_lower


def set_has_upper(has_upper):
    options_dict[Attribute.HAS_UPPER.value] = has_upper


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_help():
    print(HELP_MESSAGE)


def save_changes():
    with open('options.json', 'w') as options_json:
        json.dump(options_dict, options_json)


def execute():
    from blue_words import generate_wordlist
    generate_wordlist(options_dict)

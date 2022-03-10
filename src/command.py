from utils.string_utils import UnseenFormatter
import data

OPTIONS_STRING = '''
min_length = {min}
max_length = {max}
start_with = {start}
end_with = {end}
include = {include}
'''

formatter = UnseenFormatter()


def options():
    print(formatter.format(data.options_string))


def set_min_length(min):
    data.options_string = formatter.format(
        data.options_string, {"min": min}
    )


def set_max_length(max):
    data.options_string = formatter.format(
        data.options_string, {"max": max}
    )


def set_start_with(start):
    data.options_string = formatter.format(
        data.options_string, {"start": start}
    )


def set_end_with(end):
    data.options_string = formatter.format(
        data.options_string, {"end": end}
    )


def set_include(include):
    data.options_string = formatter.format(
        data.options_string, {"include": include}
    )



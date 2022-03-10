import command
from command import Attribute

def process(input):
    input = input.strip()
    phrase = ""
    if '"' in input:
        s_pos = input.find('"')
        e_pos = input.find('"', s_pos)
        phrase = input[s_pos + 1:e_pos]
        input = input - phrase
        input = input.strip()

    inputs = input.split(" ")
    if len(inputs) == 1:
        if inputs[0] == Attribute.OPTIONS:
            command.print_options()
        elif inputs[0] == "exit":
            return 1
        else:
            return -1
    elif len(inputs) == 2:
        if inputs[0] == "set":
            if inputs[1] == Attribute.START:
                command.set_start_with(phrase)
            elif inputs[1] == Attribute.END:
                command.set_end_with(phrase)
            elif inputs[1] == Attribute.INCLUDE:
                command.set_include(phrase)
            else:
                return -1
    elif len(inputs == 3):
        if inputs[0] == "set":
            if inputs[2].isdigit():
                if inputs[1] == Attribute.MAX:
                    command.set_max_length(inputs[2])
                elif inputs[1] == Attribute.MIN:
                    command.set_min_length(inputs[2])
                else:
                    return -1
            elif inputs[2] in ["True", "False"]:
                res = inputs[2] == "True"
                if inputs[1] == Attribute.HAS_UPPER:
                    command.set_has_upper(res)
                elif inputs[1] == Attribute.HAS_LOWER:
                    command.set_has_lower(res)
                elif inputs[1] == Attribute.HAS_SPECIAL:
                    command.set_has_special(res)
                elif inputs[1] == Attribute.HAS_DIGIT:
                    command.set_has_digit(res)
                else:
                    return -1
            else:
                return -1
    else:
        return -1
    return 0


def error(exp):
    print("bad input!")


def main():
    while True:
        try:
            res = process(input())
            if res == -1:
                error(None)
            elif res == 1:
                exit(0)
        except Exception as exp:
            error(exp)


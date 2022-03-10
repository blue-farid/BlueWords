import command


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
        if inputs[0] == "options":
            command.options()
        elif inputs[0] == "exit":
            return 1
        else:
            return -1
    if len(inputs) == 2:
        if inputs[0] == "set":
            if inputs[1] == "start_with":
                command.set_start_with(phrase)
            elif inputs[1] == "end_with":
                command.set_end_with(phrase)
            elif inputs[1] == "include":
                command.set_include(phrase)
            else:
                return -1
    if len(inputs == 3):
        if inputs[0] == "set" and inputs[2].isdigit():
            if inputs[1] == "max_length":
                command.set_max_length(inputs[2])
            elif inputs[1] == "min_length":
                command.set_min_length(inputs[2])
            else:
                return -1
    return 0


def error(exp):
    print("bad input!")


def main():
    while(True):
        try:
            res = process(input())
            if res == -1:
                error(None)
            elif res == 1:
                exit(0)
        except Exception as exp:
            error(exp)


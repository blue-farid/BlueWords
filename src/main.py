import command


def process(input):
    inputs = input.split(" ")
    if len(inputs) == 1:
        if inputs[0] == "options":
            command.options()
        else:
            print("command not found!")
            return -1
    return 0


def main():
    while(True):
        process(input())


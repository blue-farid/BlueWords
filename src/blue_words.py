import string

from command import Attribute
from pathlib import Path


def decrease_length(length, n):
    res = length - n
    if res < 0:
        res = 0
    return res


def generate_and_add_word(prefix, suffix, includes, length, k, wordlist_file):
    if k == 0:
        word = prefix + suffix + "\n"
        print(word, end="")
        wordlist_file.write(word)
        return

    for i in range(length):
        new_prefix = prefix + str(includes[i])
        generate_and_add_word(new_prefix, suffix, includes,
                              length, k - 1, wordlist_file)


def generate_wordlist(options_dict):
    word = ""
    start = options_dict[Attribute.START]
    end = options_dict[Attribute.END]
    include = options_dict[Attribute.INCLUDE]
    min_length = options_dict[Attribute.MIN]
    max_length = options_dict[Attribute.MAX]

    if start != "?":
        min_length = decrease_length(min_length, len(start))
        max_length = decrease_length(max_length, len(start))
        word = start

    if end != "?":
        min_length = decrease_length(min_length, len(end))
        max_length = decrease_length(max_length, len(end))
    else:
        end = ""

    includes = []
    if include != '?':
        includes.append(include)
    if options_dict[Attribute.HAS_LOWER]:
        includes.extend(string.ascii_lowercase)
    if options_dict[Attribute.HAS_UPPER]:
        includes.extend(string.ascii_uppercase)
    if options_dict[Attribute.HAS_DIGIT]:
        includes.extend(string.digits)
    if options_dict[Attribute.HAS_SPECIAL]:
        includes.extend(string.punctuation)

    # open the wordlist file
    path = Path("wordlist.txt")
    wordlist_file = path.open("a")

    for k in range(min_length, max_length + 1):
        generate_and_add_word(word, end, includes, len(includes), k, wordlist_file)

import string

from command import Attribute
from pathlib import Path
from more_itertools import distinct_permutations


def decrease_length(length, n):
    res = length - n
    if res < 0:
        res = 0
    return res


def generate_and_add_word(start, prefix, end, must_include, includes, length, k, wordlist_file, counter):
    if k == 0:
        if must_include != "":
            temp_list = [must_include]
            temp_list.extend(prefix)
            temp_list2 = list(distinct_permutations(temp_list))
            for word in temp_list2:
                word = start + ''.join(word) + end + "\n"
                print(word, end="")
                wordlist_file.write(word)
                counter += 1
        else:
            word = start + prefix + end + "\n"
            print(word, end="")
            wordlist_file.write(word)
            counter += 1
        return counter

    for i in range(length):
        new_prefix = prefix + str(includes[i])
        counter = generate_and_add_word(start, new_prefix, end, must_include, includes,
                                        length, k - 1, wordlist_file, counter)
    return counter


def generate_wordlist(options_dict):
    word = ""
    start = options_dict[Attribute.START.value]
    end = options_dict[Attribute.END.value]
    must_include = options_dict[Attribute.INCLUDE.value]
    min_length = options_dict[Attribute.MIN.value]
    max_length = options_dict[Attribute.MAX.value]

    if start != "?":
        min_length = decrease_length(min_length, len(start))
        max_length = decrease_length(max_length, len(start))
    else:
        start = ""

    if end != "?":
        min_length = decrease_length(min_length, len(end))
        max_length = decrease_length(max_length, len(end))
    else:
        end = ""

    includes = []
    if must_include != '?':
        min_length = decrease_length(min_length, len(must_include))
        max_length = decrease_length(max_length, len(must_include))
    else:
        must_include = ""

    if options_dict[Attribute.HAS_LOWER.value]:
        includes.extend(string.ascii_lowercase)
    if options_dict[Attribute.HAS_UPPER.value]:
        includes.extend(string.ascii_uppercase)
    if options_dict[Attribute.HAS_DIGIT.value]:
        includes.extend(string.digits)
    if options_dict[Attribute.HAS_SPECIAL.value]:
        includes.extend(string.punctuation)

    # open the wordlist file
    path = Path("wordlist.txt")
    wordlist_file = path.open("a")

    counter = 0
    for k in range(min_length, max_length + 1):
        counter += generate_and_add_word(start, word, end, must_include, includes, len(includes), k, wordlist_file, 0)
    print(f"\n{counter} words has been generated!")
    wordlist_file.close()

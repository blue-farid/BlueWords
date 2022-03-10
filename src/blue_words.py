import string

from command import Attribute


def decrease_length(length, n):
    res = length - n
    if res < 0:
        res = 0
    return res


def generate_and_add_word(prefix, includes, length, wordlist, suffix):
    if length == 0:
        wordlist.append(prefix.join(suffix))
        return

    for i in range(length):
        new_prefix = prefix.join(includes[i])
        return generate_and_add_word(new_prefix, includes,
                                     length - 1, wordlist, suffix)


def generate_wordlist(options_dict):
    wordlist = []
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
        min_length = decrease_length(min_length, len(start))
        max_length = decrease_length(max_length, len(start))

    includes = [include]
    if options_dict[Attribute.HAS_LOWER]:
        includes.extend(string.ascii_lowercase)
    if options_dict[Attribute.HAS_UPPER]:
        includes.extend(string.ascii_uppercase)
    if options_dict[Attribute.HAS_DIGIT]:
        includes.extend(string.digits)
    if options_dict[Attribute.HAS_SPECIAL]:
        includes.extend(string.punctuation)
    for length in range(min_length, max_length + 1):
        generate_and_add_word(word, includes, length,
                              wordlist, end)
    return wordlist

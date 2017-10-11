def hasher(w):  # 1
    return "".join(sorted(w))


def anagram_finder(word_list):

    hash_dict = {}  # 2

    for word in word_list:
        h = hasher(word)  # 3

        if h not in hash_dict:  # 4
            hash_dict[h] = []  # 5

        hash_dict[h].append(word)  # 6

    #return [anagram for l in hash_dict.values() for anagram in l if len(l) > 1]  # 7
    _ret = []
    for l in hash_dict.values():
        if len(l) > 1:
            _ret += l

    return _ret

if __name__ == '__main__':
    print(anagram_finder(["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]))
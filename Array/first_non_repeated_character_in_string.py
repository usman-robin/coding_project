import os
from os.path import basename
import pprint
import random

NO_OF_CHARS = 256

def main():
    str = "geeksforgeeks"
    index = find_first_non_repeated(str)

    if index:
        print (str[index])
    else:
        print None


def find_first_non_repeated(lst):
    count = [0] * NO_OF_CHARS
    index = [len(lst) + 1] * NO_OF_CHARS

    for i in range(len(lst)):
        count[ord(lst[i])] += 1

        if count[ord(lst[i])] == 1:
            index[ord(lst[i])] = i

        if count[ord(lst[i])] == 2:
            index[ord(lst[i])] = len(lst) + 1


    print(count)
    print(sorted(index))
    #print(count)

    # return the first element from the index array
    index = sorted(index)[0]

    if index == len(lst) + 1:
        return None
    else:
        return index


if __name__ == '__main__':
    main()



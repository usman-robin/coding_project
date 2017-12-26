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
    # add count array to store counts of each ascii character
    count = [0] * NO_OF_CHARS

    # add index array to store the index of singly ocurring characters
    index = [len(lst) + 1] * NO_OF_CHARS

    for i in range(len(lst)):
        # Add each character to count array
        count[ord(lst[i])] += 1

        # when count is 1 for the character add it to index array at the ascii position
        if count[ord(lst[i])] == 1:
            index[ord(lst[i])] = i

        if count[ord(lst[i])] == 2:
            index[ord(lst[i])] = len(lst) + 1

    print(count)
    for i, val  in enumerate(index):
        print("{} : {}".format(i, val))

    index = sorted(index)[0]

    if index == len(lst) + 1:
        return None
    else:
        return index

if __name__ == '__main__':
    main()



import os
from os.path import basename
import pprint
import random


def main():
    mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
    pprint.pprint(split_list(mylist, 1))


def split_list(lst, n):

    #n = len(lst)/m

    #list_of_chunks = list(lst[i:i + n] for i in range(0, len(lst), n))
    list_of_chunks = [lst[i::n] for i in range(n)]
    return list_of_chunks


if __name__ == '__main__':
    main()

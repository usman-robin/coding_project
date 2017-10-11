import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 1, 1, 6, 2, 3, 4, 4, 4, 4]

    # new_list = remove_duplicates_sorted(mylist)
    new_list = find_max_repeated(mylist)
    #print (new_list)


def find_repeated(lst):
    count = [0] * len(lst)

    for i in range(len(lst)):
        count[lst[i]] += 1

    #print(count)

    for i in range(len(count)):
        if count[i] > 1:
            print(i)


def find_max_repeated(lst):
    count = [0] * len(lst)

    for i in range(len(lst)):
        count[lst[i]] += 1

    print(count)
    max_so_far = 0
    result = None
    for i in range(len(count)):
        if max_so_far < count[i]:
            max_so_far = count[i]
            result = i

    print (result)


if __name__ == '__main__':
    main()



import os
from os.path import basename
import pprint
import random


def main():
    # mylist = [1, 2, 3, 4, 5, 6, 7, 8]

    mylist = "Let's take LeetCode contest"

    new_list = reverse_array(mylist)
    print (mylist)
    print (new_list)
    print ''.join(new_list)


def reverse_array(lst):

    lst = list(lst)

    size = len(lst)
    print(size)
    half = size / 2
    print(half)
    for i in range(size/2):
        # get element from i
        temp = lst[i]
        print("{}-{}".format(i, size - 1 - i))
        lst[i] = lst[size - 1 - i]
        # swap
        lst[len(lst) - 1 - i] = temp

    return lst

def java_style_reverse(arr):
    pass


if __name__ == '__main__':
    main()



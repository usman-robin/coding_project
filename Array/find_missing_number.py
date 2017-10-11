import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 3, 4, 6, 5]

    # new_list = remove_duplicates_sorted(mylist)
    new_list = find_missing(mylist)
    #print (new_list)


def find_missing(lst):

    # find the sum using size + 1 becuase of the missing number
    sum = (len(lst) + 1) * (len(lst) + 2) / 2
    print(sum)
    missing = None

    for i in range(len(lst)):
        sum -= lst[i]

    print(sum)


if __name__ == '__main__':
    main()



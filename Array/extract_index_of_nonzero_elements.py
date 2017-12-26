import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1,1,1,0,0,0,1,1,1]
    mylist = [1]
    mylist = [0]

    list1 = extract_non_zero_index(mylist)
    print (list1)


def extract_non_zero_index(lst):

    result = []
    mini = []
    for i in range(len(lst)):
        if lst[i]:
            mini.append(i)
        elif mini:
            result.append(mini)
            mini = []
    if mini:
        result.append(mini)

    return result


if __name__ == '__main__':
    main()



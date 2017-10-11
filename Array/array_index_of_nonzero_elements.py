import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 0, 1, 0]
    list1 = return_indices(mylist)
    list2 = getZeroIndexes(mylist)
    print(list1)
    print (list2)


def return_indices(li):
    begin = 0
    end = 0
    indexes = []

    nonzero = False
    for ind, elt in enumerate(li):

        # When you hit the first non zero
        if elt and not nonzero:
            #print("{} : {} ".format(ind, elt))
            begin = ind
            nonzero = True

        if elt and nonzero:
            end = ind
            if ind == len(li) - 1:
                indexes.append((begin, end))
            print("{} : {} ".format(ind, elt))

        if not elt and nonzero:
            nonzero = False
            if begin == end:
                indexes.append((begin, begin))
            else:
                print("IN ELSE")
                indexes.append((begin, end))

    return indexes


def getZeroIndexes(li):
    begin = 0
    end = 0
    indexes = []
    zero = False
    for ind, elt in enumerate(li):
        if not elt and not zero:
            begin = ind
            zero = True
        if not elt and zero:
            end = ind
            if ind == len(li) - 1:
                indexes.append((begin, end))
        if elt and zero:
            zero = False
            if begin == end:
                indexes.append((begin, begin))
            else:
                indexes.append((begin, end))

    return indexes

if __name__ == '__main__':
    main()



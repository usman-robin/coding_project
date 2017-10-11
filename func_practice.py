import os
from os.path import basename
import pprint


def main():
    #print(max_of_three(2, 6, 9))
    #print(sum(3, 4))
    tc_root = os.path.abspath(__file__)
    fname = os.path.splitext(tc_root)[0]
    print(tc_root)
    print(fname)
    print os.path.splitext(basename(os.path.abspath(__file__)))[0]
    print os.path.splitext(os.path.basename(__file__))[0]



def max_of_three(x, y, z):

    mylist = [x, y, z]
    mylist.sort()
    return mylist[2]


def sum(x, y):
    return x + y

if __name__ == '__main__':
    #print("hello")
    main()



import os
from os.path import basename
import pprint
from random import randrange


def main():

    mylist = []
    for i in range(10):
        mylist.append(i)

    pprint.pprint(mylist)

    for i in range(3):
        print("current index: {} element: {}".format(i, mylist[i]))
        print("next index: {} element: {}".format((i + 1) % len(mylist), mylist[(i + 1) % len(mylist)]))
        print("previous index: {} element: {}".format((i + len(mylist) - 1) % len(mylist), mylist[(i + len(mylist) - 1) % len(mylist)]))



if __name__ == '__main__':
    main()



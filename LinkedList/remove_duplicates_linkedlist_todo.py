import os
from os.path import basename
import pprint
import random
from linkedlist import OrderedList
from linkedlist import UnorderedList


def main():
    lo = OrderedList()
    lo.add(5)
    lo.add(4)
    lo.add(3)
    lo.add(4)
    lo.add(5)
    lo.add(3)
    lo.add(3)
    lo.add(3)
    lo.add(3)
    lo.add(6)
    lo.add(6)

    print("***********************")
    lo.lprint()
    print("***********************")
    #print(lo.search(40))
    print("***********************")
    # print(lo.search(8))
    # print(lo.size())
    print (lo.toArray())
    print("***********************")

    remove_duplicates_sorted(lo)
    print (lo.toArray())
    print("***********************")


def remove_duplicates_sorted(lst):

    cur = lst.head
    if cur is None:
        raise Exception("Empty List")

    while cur.getNext() is not None:
        print ("cur : {}  next : {} ".format(cur.data, cur.getNext().data))
        if cur.data == cur.getNext().data:
            print("in if")
            cur.setNext(cur.getNext().getNext())
        else:
            cur = cur.getNext()
            print("in else")
    return lst


def remove_duplicates_unsorted(lst):

    cur = lst.head

    while cur is not None:
        inner = cur
        while inner.getNext() is not None:
            print("cur {} inner {}".format(cur.data, inner.data))
            if inner.getNext().data == cur.data:
                inner.setNext(inner.getNext().getNext())
            else:
                inner = inner.getNext()
        cur = cur.getNext()

    return lst


def remove_duplicates_dict(lst):
    pass


if __name__ == '__main__':
    main()



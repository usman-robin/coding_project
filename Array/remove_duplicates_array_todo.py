import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 1, 1, 6, 2, 3, 4, 4, 4]

    #new_list = remove_duplicates_sorted(mylist)
    new_list = remove_duplicates_with_set(mylist)
    print (new_list)


def remove_duplicates_with_set(lst):

    seen = set()
    res = []

    for i in range(len(lst)):
        if lst[i] not in seen:
            res.append(lst[i])
            seen.add(lst[i])
    return res


def remove_duplicates_with_dict(lst):

    # with hash
    info = {}
    for i in range(len(lst)):
        if lst[i] in info:
            info[lst[i]] += 1
        else:
            info[lst[i]] = 0

    return info.keys()


def remove_duplicates_sorted(lst):
    newlst = sorted(lst)
    print(newlst)
    print("********")
    last = 0
    for i in range(1, len(newlst)):
        print("In the beginning i is {}".format(i))
        # Dont care about the whats left at the end of the list
        if newlst[last] != newlst[i]:
            last += 1
            newlst[last] = newlst[i]
            print("In if incrementing last:{} i:{}".format(last, i))
            print (newlst)
        else:
            #i += 1
            print("In Else Incrementing i")
    #print (newlst)
    #print(last + 1)
    return last + 1

if __name__ == '__main__':
    main()



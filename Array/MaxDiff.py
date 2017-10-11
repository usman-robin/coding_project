import os
import pprint
import sys


def main():
    lst1 = [7, 1, 5, 3, 6, 4]
    lst2 = [7, 9, 5, 6, 3, 2]
    lst3 = [2, -3, 10, 6, 4, 8, 1]
    p1 = maxdiff(lst3)
    print(p1)

def maxdiff(lst):

    (min_element, max_element) = (sys.maxint, -sys.maxint - 1)

    for val in lst:
        min_element = min(val, min_element)
        max_element= max(val, max_element)
    print("MAX : {}  MIN : {}".format(max_element, min_element))
    return max_element - min_element

if __name__ == '__main__':
    #print("hello")
    main()



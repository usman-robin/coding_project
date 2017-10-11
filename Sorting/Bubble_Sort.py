import os
from os.path import basename
import pprint
import random


def main():
    mylist = [64, 34, 25, 12, 22, 11, 90]
    new_list = bubble_sort(sorted(mylist))
    print(new_list)
    #list1 = binarySearchIterative(sorted(mylist), 13)
    #print(sorted(mylist))
    #print(list1)

# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
    # http://www.geeksforgeeks.org/bubble-sort/



if __name__ == '__main__':
    main()



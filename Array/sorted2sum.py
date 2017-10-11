import os
import pprint

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must
be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


def main():

    lst2 = [2, 7, 11, 15]
    p1 = twosumunsorted(lst2, 9)
    print (p1)


def twosum(lst, target):

    indices = []
    i = 0
    j = len(lst) - 1

    while i < j:
        if lst[i] + lst[j] == target:
            indices = [i, j]
            break
        elif lst[i] + lst[j] > target:
            j -= 1
        else:
            i += 1

    return indices


def twosumunsorted(lst, target):
    indices = []

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                continue
            elif lst[i] + lst[j] == target:
                indices = [j, i]
    return indices


if __name__ == '__main__':
    main()



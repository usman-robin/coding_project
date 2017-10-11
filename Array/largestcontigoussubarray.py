import os
import pprint


def main():
    lst2 = [-2, -3, 4, -1, -2, 1, 5, -3]
    p1 = maxsubarraysum(lst2)
    print(p1)


def maxsubarraysum(lst):
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(lst)):
        max_ending_here = max_ending_here + lst[i]

        if max_ending_here < 0:
            max_ending_here = 0

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far



if __name__ == '__main__':
    #print("hello")
    main()



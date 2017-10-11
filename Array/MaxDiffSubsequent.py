import os
import pprint


def main():
    lst1 = [7, 1, 5, 3, 6, 4]
    lst2 = [7, 9, 5, 6, 3, 2]
    lst3 = [2, 3, 10, 6, 4, 8, 1]
    p1 = maxdiff(lst2)

def maxdiff(lst):

    (max_diff, min_element) = (0, float('inf'))

    for val in lst:
        min_element = min(min_element, val)
        print("Min is {}".format(min_element))
        current_max_diff = val - min_element
        max_diff = max(max_diff, current_max_diff)
        print("MaxDiff is {}".format(max_diff))
    
    return max_diff

if __name__ == '__main__':
    #print("hello")
    main()



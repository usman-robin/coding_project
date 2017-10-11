from binary_search import bin_search

# takes 2 arrays and returns the union

# TODO unsorted


def intersection_unsorted(arr1, arr2):
    pass


def intersection_sorted(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    return result

"""
1) Initialize intersection I as empty.
2) Find smaller of m and n and sort the smaller array.
3) For every element x of larger array, do following
    b) Binary Search x in smaller array. If x is present, then copy it to I.
4) Return I.
"""
def intersection_binsearch(arr1, arr2):
    inter = []
    larger = []
    smaller = []

    if len(arr1) > len(arr2):
        larger = arr1
        smaller = arr2
    else:
        larger = arr2
        smaller = arr1

    for i in range(len(larger)):
        if bin_search(smaller, larger[i]):
            print ("Appending {} to inter".format(larger[i]))
            inter.append(larger[i])
    return inter

if __name__ == '__main__':

    arr1 = [1, 2, 3, 5, 6, 7, 13, 14, 15]
    arr2 = [4, 5, 6, 7, 8, 9, 11, 12, 13]
    #res = intersection_sorted(arr1, arr2)
    #print (res)
    res = intersection_binsearch(arr1, arr2)
    print (res)
from binary_search import bin_search
# takes 2 arrays and returns the union

# TODO unsorted


def union_unsorted(arr1, arr2):
    pass


# noinspection PyUnreachableCode
def union_sorted(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1
    print("arr1size:{} i:{} arr2size:{} j:{}".format(len(arr1), i, len(arr2), j))
    print(result)

    # Print the remaining elements
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

"""
        Union:
        1) Initialize union U as empty.
        2) Find smaller of m and n and sort the smaller array.
        3) Copy the smaller array to U.
        4) For every element x of larger array, do following
        b) Binary Search x in smaller array. If x is not present, then copy it to U.
        5) Return U.

"""


def union_binsearch(arr1, arr2):
    union = []
    larger = []
    smaller = []

    if len(arr1) > len(arr2):
        larger = arr1
        smaller = arr2
    else:
        larger = arr2
        smaller = arr1

    union = smaller

    for i in range(len(larger)):
        if not bin_search(smaller, larger[i]):
            print ("Appending {} to union".format(larger[i]))
            union.append(larger[i])
    return union


if __name__ == '__main__':
    arr1 = [1, 2, 3, 5, 6, 7]
    arr2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
    #res = union_sorted(arr1, arr2)

    res = union_binsearch(arr1, arr2)
    print (res)
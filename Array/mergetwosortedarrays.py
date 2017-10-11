from __future__ import print_function


def merge_sorted_arrays(a, b):
    c = []
    # Go until one array is empty
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    # either a or b can be not empty
    return c + a + b

if __name__ == '__main__':
    arr1 = [1, 2, 3, 5, 6, 7]
    arr2 = [8, 9, 10, 11, 12, 13]
    #res = union_sorted(arr1, arr2)

    res = merge_sorted_arrays(arr1, arr2)
    print(res)
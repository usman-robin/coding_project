# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(lst, start, end):

    i = start - 1  # index of smaller element
    pivot = lst[end]  # pivot
    print(lst)
    print("start: {} ----- end: {} ---- pivot: {}".format(start, end, pivot))
    print("")
    for j in range(start, end):

        # If current element is smaller than or
        # equal to pivot
        if lst[j] <= pivot:
            # increment index of smaller element
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# start  --> Starting index,
# end  --> Ending index

# Function to do Quick sort
def quickSort(arr, start, end):
    if start < end:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, start, end)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, start, pi - 1)
        quickSort(arr, pi + 1, end)

if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5, 3, 2]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print ("Sorted array is:")
    print(arr)
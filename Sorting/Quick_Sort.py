# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

'''
Best case and worst case
https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/analysis-of-quicksort
'''


def partition(arr, low, high):


    print("low : {}  high: {}".format(low, high))
    print(arr)
    # set lowest to -1
    i = low - 1
    j = low

    # set pivot to right most/ last element
    pivot = arr[high]

    # Scan list and swap values if less than pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # increment i, at the end loop i will point to the last small value, anything after i will be
            # greater than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            print("doing nothing")

    # swap pivot with index i + 1 to move the pivot to its right sorted index
    arr[i+1], arr[high] = arr[high], arr[i+1]

    # return the index of pivot
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# start  --> Starting index,
# end  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    #print("in quick sort")
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)


if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5, 3, 2]
    n = len(arr)
    print(n)
    quickSort(arr, 0, n - 1)
    print ("Sorted array is:")
    print(arr)

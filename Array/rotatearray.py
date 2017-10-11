"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
"""


def rotate(lst, k):
    for i in range(k):
        right_rotate(lst)


def left_rotate(lst):
    tmp = lst[0]

    for i in range(len(lst)):
        if i == len(lst) - 1:
            lst[i] = tmp
            break

        lst[i] = lst[i + 1]


def right_rotate(lst):
    tmp = lst[-1]

    for i in range(len(lst) - 1, -1, -1):
        if i == 0:
            lst[i] = tmp
            break
        lst[i] = lst[i - 1]






if __name__ == '__main__':

    lst = [1, 2, 3, 4, 5, 6, 7]
    rotate(lst, 1)
    print(lst)
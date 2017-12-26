import os
import pprint


def fib(n):
    a, b = 1, 1
    a, b = b, a + b

    print(a)
    print (b)


def fib_recursion(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fib_recursion(n - 1) + fib_recursion(n - 2)


if __name__ == '__main__':

    for i in range(8):
        print("fib {}  ::  {}".format(i, fib_recursion(i)))

    print("fib {}  ::  {}".format(6, fib_recursion(6)))
    # 0 1 1 2 3 5 8 13



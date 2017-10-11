import os
import pprint


def factorial(n):
    fact = 1

    while n >= 1:
        fact *= n
        n -= 1

    return fact


def factorial_recursion(n):

    if n <= 1:
        return 1
    return n * factorial_recursion(n - 1)


if __name__ == '__main__':
    print(factorial(5))
    print(factorial_recursion(5))



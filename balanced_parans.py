import os
from os.path import basename
import pprint
from random import randrange


def bracket_match(a, b):
    if a == '{' and b == '}':
        return True
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True

    return False


def is_balanced(expr):

    my_stack = []
    for i in expr:
        if i == '{' or i == '(' or i == '[':
            my_stack.append(i)
        elif i == '}' or i == ')' or i == ']':
            if len(my_stack) == 0:
                return False

            a = my_stack.pop()
            if bracket_match(a, i):
                continue
            else:
                return False
                #raise Exception ("Not a balanced expression")
    if len(my_stack) > 0:
        return False

    return True


def isBalanced(expr):

    if len(expr) % 2 != 0:
        return False

    opening = set('([{')
    match = {('(', ')'), ('[', ']'), ('{', '}')}
    stack = []
    for char in expr:
        print (stack)
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False

            lastOpen = stack.pop()

            if (lastOpen, char) not in match:
                return False
    print (stack)
    return len(stack) == 0


print(is_balanced("["))
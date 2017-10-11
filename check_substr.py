import os
from os.path import basename
import pprint


def main(str_to_check):

    mylist = ["ABddbdhbdbdbj", " cncncnncncncncncnc", "Hello.deleted.1232e32",]
    for item in mylist:
        if str_to_check in item:
            print("{} Matched {}".format(str_to_check, item))
        else:
            print("{} Did not match {}".format(str_to_check, item))


def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return None
    i = 0
    while i < len(haystack) - len(needle) + 1:
        j = 0
        k = i
        while j < len(needle):
            if haystack[k] == needle[j]:
                j += 1
                k += 1
            else:
                break
        if j == len(needle):
            break
        else:
            i += 1
    if i == len(haystack) - len(needle) + 1:
        return None
    else:
        return haystack[i:]


if __name__ == '__main__':
    #main("Hello.deleted")
    print(strStr("hello", "ello"))



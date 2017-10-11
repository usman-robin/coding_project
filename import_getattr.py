import os
from os.path import basename
import pprint
import random


def main():

    file_name = "factorial.py"
    testcase_module = file_name.replace(".py", "")
    import_module = __import__(testcase_module)
    print(import_module)
    testcase_class = getattr(import_module, testcase_module)
    print(testcase_class)
    testcase_obj = testcase_class(5)

    for st in dir(testcase_class):
        #continue
        print(st)

if __name__ == '__main__':
    main()



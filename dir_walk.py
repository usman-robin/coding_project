import os
import pprint


def main():
    print("hello world")
    abspath = os.path.abspath(__file__)
    currentdir = os.path.dirname(abspath)
    path = "/Users/usmansaeed/robintest/results/log"


    #pprint.pprint(abspath)
    #pprint.pprint(currentdir)
    #pprint.pprint(path)
    #print("\n\n")
    #print(type(os.walk(path)))

    for root, dirs, files in os.walk(path):
        for name in files:
            print("Name : {}".format(name))

if __name__ == '__main__':
    #print("hello")
    main()



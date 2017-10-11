import os
from os.path import basename
import pprint
from random import randrange


def main():

    mylist = []
    for i in range(1, 99):
        #print(i)
        if i % 10 == 0:
            mylist.append(i)

        if i % 33 == 0:
          random_index = randrange(0, len(mylist))
          print("##############################################")
          print("i is {}".format(i))
          pprint.pprint(mylist)
          print ("random index is : {}".format(random_index))
          s2 = mylist.pop(random_index)
          print ("removing the following element {}".format(s2))

    print("Number of elements in the array {}".format(len(mylist)))
    pprint.pprint(mylist)

if __name__ == '__main__':
    main()



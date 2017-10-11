import os
from os.path import basename
import pprint
import random

def main():

    mylist = [
    ]

    pprint.pprint(mylist)
    if any("test_vol_a.deleted.1468910279" == d['name'] for d in mylist):
      #print(d['name'])
      print("True")
      pass
    else:
      pass
      #print("False")

    new_list = random.choice(mylist)
    new_list['block_size'] = 40000
    pprint.pprint(mylist)



if __name__ == '__main__':
    main()



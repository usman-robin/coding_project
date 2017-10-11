import os
from os.path import basename
import pprint
import random

def main():

    mylist = [
                {u'asize': 15032385536,
                  u'block_size': 4096,
                  u'compress_algo': 1,
                  u'ctime': 0,
                  u'current_snapshotid': 2,
                  u'lsize': 21474836480,
                  u'media': 72,
                  u'name': u'test_vol_b.deleted.1468910279',
                  u'poolid': 1,
                  u'protection': 0,
                  u'psize': 503316480,
                  u'qgroupid': 1,
                  u'replication': 1,
                  u'rsize': 21474836480,
                  u'slice_size': 1073741824,
                  u'state': 5,
                  u'status': 1,
                  u'volumeid': 1,
                  u'vtype': 0},

                  {u'asize': 15032385536,
                  u'block_size': 4096,
                  u'compress_algo': 1,
                  u'ctime': 0,
                  u'current_snapshotid': 2,
                  u'lsize': 21474836480,
                  u'media': 72,
                  u'name': u'test_vol_a.deleted.1468910279',
                  u'poolid': 1,
                  u'protection': 0,
                  u'psize': 503316480,
                  u'qgroupid': 1,
                  u'replication': 1,
                  u'rsize': 21474836480,
                  u'slice_size': 1073741824,
                  u'state': 5,
                  u'status': 1,
                  u'volumeid': 1,
                  u'vtype': 0},
    ]

    pprint.pprint(mylist)
    if any("test_vol_a.deleted.1468910279" == d['name'] for d in mylist):
      #print(d['name'])
      #print("True")
      pass
    else:
      pass
      #print("False")

    new_list = random.choice(mylist)
    new_list['block_size'] = 40000
    pprint.pprint(mylist)


if __name__ == '__main__':
    main()



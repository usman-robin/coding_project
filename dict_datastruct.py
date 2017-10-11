import os
from os.path import basename
import pprint
import random

def main():

    lst = []

    info = {"devs":[{"devid":12,"bmaps":[]},{"devid":22,"bmaps":[]},{"devid":14,"bmaps":[]},{"devid":17,"bmaps":[]},{"devid":21,"bmaps":[]},{"devid":15,"bmaps":[]},{"devid":19,"bmaps":[]},{"devid":16,"bmaps":[]},{"devid":18,"bmaps":[]},{"devid":20,"bmaps":[{"volumeid":7,"snapshotid":1,"slice_loffset":0,"segseqnum":1001,"seg_index_offset":33546304,"state":"BMAP_READY","epoch":1}]},{"devid":13,"bmaps":[]}]}


    pprint.pprint(info)

    for dev in info['devs']:
        for bmap in dev['bmaps']:
            bmap['devid'] = dev['devid']
            lst.append(bmap)
    pprint.pprint(lst)


if __name__ == '__main__':
    main()



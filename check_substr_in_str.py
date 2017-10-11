import os
from os.path import basename
import pprint


def main(str_to_check):

    str = ' appid | volumeid |    name    |    size     | block_size | slice_size | fssize | fsfree | replication |' \
          ' media | vtype | protection | current_snapshotid | next_snapshotid | compress | multinode_mounting | params ' \
          '|   ctime    | state | status | zoneid | nodeid |      genkey      | parent_appid | ' \
          'parent_volumeid | parent_snapshotid | qgroupid | respoolid | partitions | volgroupid \n-------+----------+---' \
          '---------+-------------+------------+------------+--------+--------+-------------+-------+-------+---------' \
          '---+--------------------+-----------------+----------+--------------------+--------+------------+-------+---' \
          '-----+--------+--------+------------------+--------------+-----------------+-------------------+----------+--' \
          '---------+------------+------------\n     1 |        4 | clone_9OlO.deleted | 21474836480 |    ' \
          '   4096 | 1073741824 |      0 |      0 |           1 |    72 |     1 |          0 |                  1 |   ' \
          '            2 |        1 |                  0 | {}     | 1478553920 |     2 |      1 |        |   ' \
          '     | 1478553920002457 |            1 |               3 |                 1 |        1 |         1 |   ' \
          '       0 |          0\n(1 row)\n\n'

    if str_to_check in str:
        print("{} Matched".format(str_to_check))
    else:
        print("{} Did not match".format(str_to_check))

if __name__ == '__main__':
    main("clone_9OlO")



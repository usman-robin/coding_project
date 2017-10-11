import os
import pprint
import time


def main():
    wait_until_done()


def wait_until_done(timeout=15):
    start_time = time.time()

    while time.time() < (start_time + timeout):
        lst_of_sets = []
        ready_counter = 0
        not_ready_counter = 0
        data = { 'appid': 1,
                 'appname': 'default',
                 'nallocated': 20,
                 'nslices': 20,
                 'replication': 2,
                 'slices': [{'generation': 1,
                              'loffset': 0,
                              'replicas': [{'devid': 10,
                                             'generation': 1,
                                             'leader': 1,
                                             'nodeid': 3,
                                             'segcnt': 1,
                                             'sliceidx': 0,
                                             'state': 'READY',
                                             'zoneid': 1500602242},
                                            {'devid': 16,
                                             'generation': 3,
                                             'leader': 0,
                                             'nodeid': 5,
                                             'segcnt': 1,
                                             'sliceidx': 0,
                                             'state': 'RESYNC',
                                             'zoneid': 1500602242}],
                              'state': 'DEGRADED',
                              'version': 1},
                             {'generation': 1,
                              'loffset': 1073741824,
                              'replicas': [{'devid': 10,
                                             'generation': 1,
                                             'leader': 1,
                                             'nodeid': 3,
                                             'segcnt': 1,
                                             'sliceidx': 4,
                                             'state': 'READY',
                                             'zoneid': 1500602242},
                                            {'devid': 16,
                                             'generation': 1,
                                             'leader': 0,
                                             'nodeid': 5,
                                             'segcnt': 1,
                                             'sliceidx': 4,
                                             'state': 'READY',
                                             'zoneid': 1500602242}],
                              'state': 'READY',
                              'version': 1},
                            {'generation': 1,
                             'loffset': 1073741824,
                             'replicas': [{'devid': 10,
                                           'generation': 1,
                                           'leader': 1,
                                           'nodeid': 3,
                                           'segcnt': 1,
                                           'sliceidx': 4,
                                           'state': 'READY',
                                           'zoneid': 1500602242},
                                          {'devid': 16,
                                           'generation': 1,
                                           'leader': 0,
                                           'nodeid': 5,
                                           'segcnt': 1,
                                           'sliceidx': 4,
                                           'state': 'READY',
                                           'zoneid': 1500602242}],
                             'state': 'READY',
                             'version': 1},
                             {'generation': 1,
                              'loffset': 2147483648,
                              'replicas': [{'devid': 10,
                                             'generation': 1,
                                             'leader': 1,
                                             'nodeid': 3,
                                             'segcnt': 1,
                                             'sliceidx': 2,
                                             'state': 'READY',
                                             'zoneid': 1500602242},
                                            {'devid': 16,
                                             'generation': 1,
                                             'leader': 0,
                                             'nodeid': 5,
                                             'segcnt': 1,
                                             'sliceidx': 2,
                                             'state': 'READY',
                                             'zoneid': 1500602242}],
                              'state': 'READY',
                              'version': 1}]

                 }

        for s in data["slices"]:
            my_set = set()
            for r in s["replicas"]:
                k = r["generation"]
                s = r["state"]
                my_set.add((k, s))
            #print(type(my_set))
            #print(my_set)
            #print (len(my_set))
            if len(my_set) > 1:
                lst_of_sets.append(my_set)
                ready_counter += len(my_set)

        if len(lst_of_sets) == 0:
            print("RETURNING from set size 0")
            return

        for s in lst_of_sets:
            for tup in s:
                if tup[1] == "READY":
                    continue
                else:
                    print("Not Ready")
                    not_ready_counter += 1

        if not_ready_counter == 0:
            print("RETURNING from not_ready_counter")
            print(not_ready_counter)
            return

        print("Sleeping for 3 seconds")
        time.sleep(3)

    raise Exception("Could not return in {} seconds".format(timeout))

if __name__ == '__main__':
    #print("hello")
    main()



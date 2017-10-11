import pprint
import time
import multiprocessing
from multiprocessing import Queue
from random import randint


def f(q, arr):
    q.put(arr)


class RobinCHOProcess(multiprocessing.Process):
    def __init__(self, name, queue):
        super(RobinCHOProcess, self).__init__()
        self.name = name
        self.queue = queue

    def run(self):
        hptr = {
                "thread_name" : self.name,
                "thread_id" :randint(0, 9)
        }
        self.queue.put(hptr)

if __name__ == '__main__':
    q1 = Queue()
    prcs = []

    for i in range(0, 3):
        p = RobinCHOProcess("thread_{}".format(i), q1)
        p.start()
        prcs.append(p)

    for p in prcs:
        p.join()
        print("{} exitcode = {}".format(p.name, p.exitcode))

    while not q1.empty():
        pprint.pprint(q1.get())    # prints "[42, None, 'hello']"



#!/usr/bin/python

import threading
import time
import pprint


exitFlag = 0


class myThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 10)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    time.sleep(30)

# Create new threads
thread1 = myThread(1, "Thread-1", 1)


# Start new Threads
thread1.start()
pprint.pprint(threading.enumerate())
#thread1.join()

thread1.join(timeout=5)
if thread1.isAlive():
    print("I am in is alive")
    raise ValueError("Thread 1 is still alive")



print "Exiting Main Thread"

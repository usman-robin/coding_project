#!/usr/bin/python
import threading
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class Counter(object):

    def __init__(self, start=0):
        self.value = start
        self.lock = threading.Lock()

    def get_lock(self):
        return self.lock

    def get_count(self):
        return self.count

    def increment(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired a lock')
            self.value += 1
            time.sleep(3)
        finally:
            logging.debug('Released a lock')
            self.lock.release()


def worker(c):
    for i in range(2):
        r = random.random()
        #logging.debug('Sleeping %0.02f', r)
        time.sleep(r)
        c.increment()
    logging.debug('Done')


if __name__ == '__main__':

    counter = Counter()
    threads = []
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()
        threads.append(t)

    logging.debug('Waiting for worker threads')
    for t in threads:
        t.join()
    logging.debug('Counter: %d', counter.value)







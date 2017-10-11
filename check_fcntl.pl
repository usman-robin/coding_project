#/usr/bin/perl
import fcntl
import time
import errno

def check_fcntl():
    start_time = time.time()
    lockfile = "/tmp/check.lock"
    fp = open(lockfile, 'a')
    while True:
        try:
            fcntl.flock(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except IOError as e:
            # raise on unrelated IOErrors
            if e.errno != errno.EAGAIN:
                raise
            else:
                time.sleep(0.1)
    print("Sleeping for 30 seconds")
    time.sleep(30)
    fcntl.flock(fp, fcntl.LOCK_UN)

    end_time = time.time()
    elapsed =  end_time - start_time
    print("The program ran for {} seconds".format(elapsed))

if __name__ == '__main__':
    check_fcntl()

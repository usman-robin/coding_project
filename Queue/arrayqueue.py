
class Queue(object):

    def __init__(self, size=5):
        self.arr = [None] * size
        self.front = len(self.arr) * 2
        self.end = len(self.arr) * 2

    def is_full(self):
        # check if end is at the last index
        return self.end + 1 == len(self.arr)

    def is_empty(self):
        return self.end == len(self.arr) * 2 and self.front == len(self.arr) * 2
    
    def put(self, data):
        # if array is full raise exception

        if self.is_full():
            raise Exception("Queue is full")

        # if queue is empty set the end and front to 0
        elif self.is_empty():
            self.front = 0
            self.end = 0
        # normal case:  increment end
        else:
            self.end += 1

        # write data at the updated end
        self.arr[self.end] = data
        print("After put")
        print("front : {}".format(self.front))
        print("end : {}".format(self.end))
        print(self.arr)

    def take(self):
        data = None
        # if queue is empty raise exception
        if self.is_empty():
            raise Exception("Queue is empty")

        # if end == front, reset both to illegal index
        # this means only one element left in the
        elif self.front == self.end:
            data = self.arr[self.front]
            self.front = self.end = len(self.arr) * 2
            print("After take")
            print("front : {}".format(self.front))
            print("end : {}".format(self.end))
            print(self.arr)
            return data

        # normal case: take the element from the front of the queue and increment front
        else:
            data = self.arr[self.front]
            self.front += 1
            print("After take")
            print("front : {}".format(self.front))
            print("end : {}".format(self.end))
            print(self.arr)
            return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty cannot peek")
        return self.arr[self.front]

    def qprint(self):
        if self.is_empty():
            raise Exception("Cannot print empty queue")
        print("qprint")
        print("front : {}".format(self.front))
        print("end : {}".format(self.end))
        for i in range(self.front, self.end + 1):
            print (self.arr[i])
        print(self.arr)

    def clear(self):
        self.end = self.front = len(self.arr) * 2


class CircularQueue:

    def __init__(self, size=5):
        self.arr = [None] * size
        self.front = len(self.arr) * 2
        self.end = len(self.arr) * 2

    def is_full(self):
        # check if end is at the last index
        return (self.end + 1) % len(self.arr) == self.front

    def is_empty(self):
        return self.end == len(self.arr) * 2 and self.front == len(self.arr) * 2

    def put(self, data):
        # if array is full raise exception

        if self.is_full():
            raise Exception("Queue is full")

        # if queue is empty set the end and front to 0
        elif self.is_empty():
            self.front = 0
            self.end = 0
        # normal case:  increment end
        else:
            self.end = (self.end + 1) % len(self.arr)

        # write data at the updated end
        self.arr[self.end] = data
        print("After put")
        print("front : {}".format(self.front))
        print("end : {}".format(self.end))
        print(self.arr)

    def take(self):
        data = None
        # if queue is empty raise exception
        if self.is_empty():
            raise Exception("Queue is empty")

        # if end == front, reset both to illegal index
        # this means only one element left in the
        elif self.front == self.end:
            data = self.arr[self.front]
            self.front = self.end = len(self.arr) * 2
            print("After take")
            print("front : {}".format(self.front))
            print("end : {}".format(self.end))
            print(self.arr)
            return data

        # normal case: take the element from the front of the queue and increment front
        else:
            data = self.arr[self.front]
            self.front = (self.front + 1) % len(self.arr)
            print("After take")
            print("front : {}".format(self.front))
            print("end : {}".format(self.end))
            print(self.arr)
            return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty cannot peek")
        return self.arr[self.front]
    
q = CircularQueue()

for i in range(1):
    for i in range(5):
        q.put(i)
    for i in range(3):
        q.take()
    for i in range(3):
        q.put(i)
while not q.is_empty():

    print(q.take())

    #print(q.peek())
#q.put(2)
#q.put(3)
#q.put(4)
#q.put(5)
#q.take()


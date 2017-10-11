
class Stack(object):

    def __init__(self, size=5):
        self.arr = [None] * size
        self.top = len(self.arr) * 2

    def is_full(self):
        # check if end is at the last index
        return self.top + 1 == len(self.arr)

    def is_empty(self):
        return self.top == len(self.arr) * 2
    
    def push(self, data):
        # if array is full raise exception

        if self.is_full():
            raise Exception("Stack is full")

        # if stack is empty set the end and top to 0
        elif self.is_empty():
            self.top = 0
        # normal case:  increment end
        else:
            self.top += 1

        # write data at the updated end
        self.arr[self.top] = data
        print("After push")
        print("top : {}".format(self.top))
        print(self.arr)

    def pop(self):
        data = None
        # if stack is empty raise exception
        if self.is_empty():
            raise Exception("stack is empty")

        # if end == top, reset both to illegal index
        # this means only one element left in the
        elif self.top == 0:
            data = self.arr[self.top]
            self.top = len(self.arr) * 2
            print("After take")
            print("top : {}".format(self.top))
            print(self.arr)
            #self.stackprint()
            return data

        # normal case: take the element from the top of the stack and increment top
        else:
            data = self.arr[self.top]
            self.top -= 1
            print("After take")
            print("top : {}".format(self.top))
            print(self.arr)
            self.stackprint()
            return data

    def top(self):
        if self.is_empty():
            raise Exception("stack is empty cannot peek")
        return self.arr[self.top]

    def clear(self):
        self.top = len(self.arr) * 2

    def stackprint(self):
        if self.is_empty():
            raise Exception("Stack is empty cannot print")
        stack = []
        for i in range(self.top + 1):
            stack.append(self.arr[i])
        print(stack)

q = Stack()

for i in range(1):
    for i in range(5):
        q.push(i)
    print("Popping 3")
    for i in range(3):
        q.pop()
    print("Pushing 3")
    for i in range(2, 5):
        q.push(i)
while not q.is_empty():
    print(q.pop())
    q.stackprint()

    #print(q.peek())
#q.put(2)
#q.put(3)
#q.put(4)
#q.put(5)
#q.take()


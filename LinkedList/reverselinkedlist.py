from node import Node


class OrderedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, val):

        # search for the element

        cur = self.head
        previous = None
        stop = False

        while cur is not None and not stop:
            if cur.getData() > val:
                stop = True
            else:
                previous = cur
                cur = cur.getNext()

        temp = Node(val)

        # check to see if empty linked list
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(cur)
            previous.setNext(temp)

    def remove(self, val):

        if self.search(val) is False:
            raise Exception("Cannot remove, element does not exist")

        # search for the element
        found = False
        cur = self.head
        previous = None

        while not found:
            if cur.getData() == val:
                found = True
            else:
                previous = cur
                cur = cur.getNext()

        if previous is None:
            self.head = cur.getNext()
        else:
            previous.setNext(cur.getNext())

    def size(self):
        sz = 0
        if self.isEmpty():
            sz = 0
        cur = self.head

        while cur is not None:
            sz += 1
            cur = cur.getNext()
        return sz

    def search(self, val):
        counter = 0
        found = False
        stop = False
        cur = self.head

        while cur is not None and not found and not stop:
            counter += 1

            if cur.getData() == val:
                found = True
            elif cur.getData() > val:
                print("in here")
                stop = True
            else:
                cur = cur.getNext()

        print(counter)
        return found

    def reverse(self):
        cur = self.head
        previous = None

        while cur is not None:
            next = cur.getNext()
            cur.setNext(previous)
            previous = cur
            cur = next

            #print("cur:{} pre:{} next:{}".format(cur.data, previous.data, next.data))

        self.head = previous

    def toArray(self):
        lst = []
        cur = self.head
        while cur is not None:
            lst.append(cur.getData())
            cur = cur.getNext()
        return lst

    def lprint(self):
        cur = self.head
        while cur is not None:
            print(cur.getData())
            cur = cur.getNext()

if __name__ == '__main__':
    lo = OrderedList()
    lo.add(1)
    lo.add(2)
    lo.add(3)
    lo.add(4)
    lo.add(5)
    lo.add(7)
    lo.add(8)
    print("***********************")
    print(lo.toArray())
    print("***********************")
    lo.reverse()
    print("***********************")

    print(lo.toArray())
    print("***********************")

from linkedlist import Node
from linkedlist import OrderedList


def find_middle(ll):
    fast = ll.head
    slow = ll.head

    #while fast is not None and fast.next is not None:
    while fast is not None:
        print("Before Slow: {}     Fast: {}".format(slow.data, fast.data))
        slow = slow.next
        fast = fast.next.next
        if fast is not None:
            print("After  Slow: {}     Fast: {}".format(slow.data, fast.data))
            print("\n")
    return slow


if __name__ == '__main__':
    lo = OrderedList()
    lo.add(1)
    lo.add(2)
    lo.add(3)
    lo.add(4)
    lo.add(5)
    lo.add(7)
    lo.add(8)
    lo.add(9)
    print("***********************")
    print(lo.toArray())
    print("***********************")
    mid = find_middle(lo)
    print("***********************")

    print(mid.data)
    print("***********************")

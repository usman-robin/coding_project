from linkedlist import UnorderedList
import sys


def find_loop(ll):
    slow = ll.head
    fast = ll.head
    has_loop = False
    while fast.next is not None and fast.next.next is not None:

        slow = slow.next
        fast = fast.next.next
        print("Fast:  {}    Slow:  {}".format(fast.data, slow.data))
        if slow.data == fast.data:
            has_loop = True
            break

    return has_loop
if __name__ == '__main__':
    lo = UnorderedList()
    lo.add(1)
    lo.add(3)
    lo.add(2)
    lo.add(15)
    lo.add(5)
    lo.add(10)
    lo.add(7)
    lo.add(8)

    cur = lo.head
    center = None
    while cur.next is not None:
        if cur.data == 15:
            center = cur
        cur = cur.next

    cur.setNext(center)


    print("***********************")
    print(find_loop(lo))
    #print(lo.lprint())
    #print(lo.toArray())
    print("***********************")
    print("***********************")

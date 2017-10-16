from linkedlist import UnorderedList
import sys


def remove_minimum(ll):
    cur = ll.head
    prev = None
    smallest_data = sys.maxint
    smallest_so_far = None
    prev_to_smallest_so_far = None
    while cur is not None:
        print(cur.data)
        if cur.getData() < smallest_data:
            smallest_data = cur.getData()
            print("In here {}".format(cur.data))
            smallest_so_far = cur
            prev_to_smallest_so_far = prev

        prev = cur
        cur = cur.next
    # if the smallest element is at the head of the linked list:
    if prev_to_smallest_so_far is None:
        ll.head = smallest_so_far.getNext()
        smallest_so_far = None
    else:
        prev_to_smallest_so_far.setNext(smallest_so_far.getNext())
    #print("Previous {}  Smallest {}".format(prev_to_smallest_so_far.data, smallest_so_far.data))

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
    lo.add(15)
    print("***********************")
    print(lo.lprint())
    print(lo.toArray())
    print("***********************")
    print("***********************")
    remove_minimum(lo)
    print(lo.toArray())
    print("***********************")

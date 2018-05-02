#Given a linked list, remove the nth node from the end of list and return its
#head.

from LinkedList import LinkedList
from LinkedList import ListNode

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        second = head

        i = 0
        while first.next is not None and i < n:
            first = first.next
            i += 1

        while first.next is not None:
            first = first.next
            second = second.next

        if i != n:
            head = second.next
        else:
            second.next = second.next.next
        return head

if __name__ == "__main__":
    arrayA = [int(x) for x in input().strip().split(',')]
    n = int(input().strip())

    listA = LinkedList()

    for element in arrayA:
        listA.push(element)

    listC = LinkedList()
    listC.head = Solution().removeNthFromEnd(listA.head, n)

    listC.printList()

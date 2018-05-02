#Given a list, rotate the list to the right by k places, where k is
#non-negative.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import LinkedList
from LinkedList import ListNode
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None or k == 0:
            return head

        first = head
        second = head

        i = 0
        while i < k:
            try:
                first = first.next
                i += 1
            except AttributeError:
                k %= i
                i = 0
                first = head

        if first is None or first == second:
            return head

        while first.next:
            first = first.next
            second = second.next

        head, first.next = second.next, head
        second.next = None

        return head

if __name__ == "__main__":
    array = [int(x) for x in input().strip().split(',')]
    k = int(input().strip())
    listA = LinkedList()

    for element in array:
        listA.push(element)

    listB = LinkedList()

    listB.head = Solution().rotateRight(listA.head, k)

    listB.printList()

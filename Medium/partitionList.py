#Given a linked list and a value x, partition it such that all nodes less than x
#come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two
#partitions.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import LinkedList
from LinkedList import ListNode
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        tempNodeL = ListNode(0)
        tempNodeH = ListNode(0)

        headL = tempNodeL
        headH = tempNodeH

        while head:
            if head.val < x:
                tempNodeL.next = head
                tempNodeL = tempNodeL.next
            else:
                tempNodeH.next = head
                tempNodeH = tempNodeH.next

            head = head.next

        tempNodeH.next = None
        tempNodeL.next = headH.next

        return headL.next

if __name__ == "__main__":
    arrayA = [int(x) for x in input().strip().split(',')]
    x = int(input().strip())

    listA = LinkedList()

    for elem in arrayA:
        listA.push(elem)

    listB = LinkedList()

    listB.head = Solution().partition(listA.head, x)

    listB.printList()

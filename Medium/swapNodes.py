#Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import LinkedList
from LinkedList import ListNode

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        tempNode = ListNode(0)
        pre,pre.next = tempNode, head

        while pre.next is not None and pre.next.next is not None:
            a = pre.next
            b = a.next

            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return tempNode.next

if __name__ == "__main__":
    arrayA = [int(x) for x in input().strip().split(',')]

    listA = LinkedList()
    for element in arrayA:
        listA.push(element)

    listB = LinkedList()
    listB.head = Solution().swapPairs(listA.head)
    listB.printList()

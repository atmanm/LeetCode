#Write a program to find the node at which the intersection of two singly linked
#lists begins.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import LinkedList
from LinkedList import ListNode

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA is None or headB is None:
            return None

        runner1 = headA
        runner2 = headB

        while runner1 is not runner2:
            if runner1 is None:
                runner1 = headB
            elif runner2 is None:
                runner2 = headA
            else:
                runner1 = runner1.next
                runner2 = runner2.next

        return runner1

if __name__ == "__main__":
    arrayA = [int(x) for x in input().strip().split(',')]
    arrayB = [int(x) for x in input().strip().split(',')]

    listA = LinkedList()
    listB = LinkedList()

    for element in reversed(arrayA):
        listA.push(element)

    for element in reversed(arrayB):
        listB.push(element)

    print(Solution().getIntersectionNode(listA.head, listB.head).val)

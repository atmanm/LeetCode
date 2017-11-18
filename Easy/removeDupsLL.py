#Given a sorted linked list, delete all duplicates such that each element appear
#only once.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from  LinkedList import ListNode
from  LinkedList import LinkedList
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        data = head.val
        curNode = head
        firstOcc = head

        while curNode != None:
            if curNode.val != data:
                data = curNode.val
                firstOcc.next = curNode
                firstOcc = curNode

            curNode = curNode.next

        if firstOcc is not None:
            firstOcc.next = None

        return head

if __name__ == "__main__":
    try:
        l1Array = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        l1Array = []

    l1 = LinkedList()
    for x in reversed(l1Array):
        l1.push(x)

    retHead = Solution().deleteDuplicates(l1.head)
    l1.head = retHead
    l1.printList()

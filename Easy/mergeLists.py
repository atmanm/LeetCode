#Merge two sorted linked lists and return it as a new list. The new list should
#be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from  LinkedList import ListNode
from  LinkedList import LinkedList
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        retHead = None
        curNodel1 = l1
        curNodel2 = l2
        curNodeRet = None
        while curNodel1 and curNodel2:
            if curNodel1.val < curNodel2.val:
                if retHead is None:
                    retHead = curNodel1
                else:
                    curNodeRet.next = curNodel1
                curNodeRet = curNodel1
                curNodel1 = curNodel1.next
            else:
                if retHead is None:
                    retHead = curNodel2
                else:
                    curNodeRet.next = curNodel2
                curNodeRet = curNodel2
                curNodel2 = curNodel2.next

        while curNodel1:
            if retHead is None:
                retHead = curNodel1
            else:
                curNodeRet.next = curNodel1
            curNodeRet = curNodel1
            curNodel1 = curNodel1.next

        while curNodel2:
            if retHead is None:
                retHead = curNodel2
            else:
                curNodeRet.next = curNodel2
            curNodeRet = curNodel2
            curNodel2 = curNodel2.next

        return retHead


if __name__ == "__main__":
    try:
        l1Array = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        l1Array = []
    try:
        l2Array = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        l2Array = []

    l1 = LinkedList()
    for x in reversed(l1Array):
        l1.push(x)

    l2 = LinkedList()
    for x in reversed(l2Array):
        l2.push(x)

    retHead = Solution().mergeTwoLists(l1.head, l2.head)
    l1.head = retHead
    l1.printList()

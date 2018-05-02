# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import LinkedList
from LinkedList import ListNode
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        tempNode = ListNode(0)
        tempNode.next = head

        cur = head
        prev = tempNode
        while cur.next is not None:
            if cur.val != cur.next.val:
                remove = False
                if prev.next == cur:
                    prev = prev.next
                else:
                    prev.next = cur.next
            else:
                remove = True
            cur = cur.next

        if remove:
            prev.next = cur.next
        return tempNode.next

if __name__ == "__main__":
    arrayA = [int(x) for x in input().strip().split(',')]

    listA = LinkedList()

    for elem in arrayA:
        listA.push(elem)

    listB = LinkedList()
    listB.head = Solution().deleteDuplicates(listA.head)

    listB.printList()

#Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import ListNode
from LinkedList import LinkedList

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast is not None:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return False

            if fast is slow:
                return True

        return False

if __name__ == "__main__":
    try:
        array = [int(x) for x in input().strip().split(',')]
    except ValueError:
        array = []

    LList = LinkedList()
    for val in reversed(array):
        LList.push(val)
    LList.printList()
    print(Solution().hasCycle(LList.head))

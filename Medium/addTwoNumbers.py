#You are given two non-empty linked lists representing two non-negative
#integers. The digits are stored in reverse order and each of their nodes contain
#a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the
#number 0 itself.

from LinkedList import LinkedList
from LinkedList import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        sumList = LinkedList()

        while l1 and l2:
            newNode = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry)//10

            sumList.push(newNode)
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                newNode = ListNode((l1.val+carry)%10)
                carry = (l1.val+carry)//10

                sumList.push(newNode)
                l1 = l1.next
        elif l2:
            while l2:
                newNode = ListNode((l2.val+carry)%10)
                carry = (l2.val+carry)//10

                sumList.push(newNode)
                l2 = l2.next

        if carry:
            newNode = ListNode(carry)
            sumList.push(newNode)

        return sumList.head

if __name__ == "__main__":
    arrayA = [int(x) for x in input().strip().split(',')]
    arrayB = [int(x) for x in input().strip().split(',')]

    listA = LinkedList()
    listB = LinkedList()

    for element in arrayA:
        listA.push(element)

    for element in arrayB:
        listB.push(element)

    listC = LinkedList()
    listC.head = Solution().addTwoNumbers(listA.head, listB.head)

    listC.printList()

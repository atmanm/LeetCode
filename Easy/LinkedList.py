class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = ListNode(new_val)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        print ("List:")
        temp = self.head
        while(temp):
            print(temp.val, end=' ')
            temp = temp.next
        print("")

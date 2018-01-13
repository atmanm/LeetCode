class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_val):
        new_node = ListNode(new_val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def printList(self):
        print ("List:")
        temp = self.head
        while(temp):
            print(temp.val, end=' ')
            temp = temp.next
        print("")

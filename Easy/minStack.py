#Design a stack that supports push, pop, top, and retrieving the minimum element
#in constant time.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #Will hold a tuple of (value, min so far)
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        try:
            curMin = self.getMin()
        except AttributeError:
            curMin = x
        if x < curMin:
            self.stack.append((x,x))
        else:
            self.stack.append((x,curMin))

    def pop(self):
        """
        :rtype: void
        """
        val,curMin = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        try:
            val,curMin = self.stack[-1]
        except IndexError:
            return None
        return val

    def getMin(self):
        """
        :rtype: int
        """
        try:
            val,curMin = self.stack[-1]
        except IndexError:
            return None
        return curMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    myStack = MinStack()
    myStack.push(-2)
    myStack.push(0)
    myStack.push(-3)
    print(myStack.getMin())
    myStack.pop()
    print(myStack.top())
    print(myStack.getMin())

#Write an algorithm to determine if a number is "happy".
#A happy number is a number defined by the following process: Starting with any
#positive integer, replace the number by the sum of the squares of its digits,
#and repeat the process until the number equals 1 (where it will stay), or it
#loops endlessly in a cycle which does not include 1. Those numbers for which
#this process ends in 1 are happy numbers.

class Solution(object):
    def findSumSquare(self, n):
        curSum = 0
        while n > 0:
            curSum += (n%10)**2
            n //= 10
        return curSum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while True:
            slow = self.findSumSquare(slow)
            fast = self.findSumSquare(fast)
            fast = self.findSumSquare(fast)
            if fast == 1:
                return True
            if slow == fast:
                return False

if __name__ == "__main__":
    num = int(input().strip())
    print(Solution().isHappy(num))

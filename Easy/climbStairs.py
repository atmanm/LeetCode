#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you
#climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

#        numWays = self.findWays(n)
#        return numWays
#
#    def findWays(self, n):
#        if n == 0:
#            return 0
#        elif n == 1:
#            return 1
#        elif n == 2:
#            return 2
#        else:
#            return self.findWays(n-1) + self.findWays(n-2)

        a = 0
        b = 1
        for _ in range(n):
            b,a = a+b,b

        return b

if __name__ == "__main__":
    n = int(input())

    print(Solution().climbStairs(n))

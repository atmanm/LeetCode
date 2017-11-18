#Implement int sqrt(int x).
#Compute and return the square root of x.
#x is guaranteed to be a non-negative integer.
class Solution(object):
    def mySqrt(self, S):
        """
        :type x: int
        :rtype: int
        """

        #Newton-Raphson method of approximation to find solution for f(x) = 0
        # x2 = x1 - f(x1)/f'(x1)
        # For Square root, equation to solve is x**2 - S = 0
        # x2 = x1 - (x1**2 - S)/2*x1
        # x2 = (2*x1**2 - x1**2 + S)/(2*x1)
        # x2 = (x1**2 + S)/(2*x1)
        # x2 = (x1 + S/x1)/2
        # Repeat with x2 as new x1
        # Keep doing this till you're happy (x1**2 is close enough to S)
        x = S
        while x**2 > S:
            print(x)
            x = (x+S/x)/2

        return int(x)

#        if x == 0:
#            return 0
#        return self.binarySearch(0, x, x)
#
#    def binarySearch(self, startIdx, endIdx, target):
#        if startIdx == endIdx or endIdx == startIdx + 1:
#            return startIdx + 1
#
#        midIdx = int((startIdx + endIdx)/2)
#        midElem = midIdx + 1
#
#        if midElem**2 == target:
#            return midIdx + 1
#        elif midElem**2 < target:
#            return self.binarySearch(midIdx, endIdx, target)
#        else:
#            return self.binarySearch(startIdx, midIdx, target)


if __name__ == "__main__":
    target = int(input())

    print(Solution().mySqrt(target))

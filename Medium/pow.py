#Implement pow(x, n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1.0/x
            n = abs(n)
        result = float(1)
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result

if __name__ == "__main__":
    x = float(input().strip())
    n = int(input().strip())
    print(Solution().myPow(x,n))

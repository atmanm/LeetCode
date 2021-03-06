#Given an integer n, return the number of trailing zeroes in n!.
#Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n//5 + self.trailingZeroes(n//5)

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().trailingZeroes(n))

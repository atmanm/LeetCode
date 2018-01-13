#Write a function that takes an unsigned integer and returns the number of ’1'
#bits it has (also known as the Hamming weight).

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n % 2
            n //= 2
        return count

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().hammingWeight(n))

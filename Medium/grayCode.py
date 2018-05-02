#The gray code is a binary numeral system where two successive values differ in
#only one bit.
#Given a non-negative integer n representing the total number of bits in the
#code, print the sequence of gray code. A gray code sequence must begin with 0.

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        retList = self.grayCodeHelper(n)
        return [int(x,2) for x in retList]

    def grayCodeHelper(self, n):
        if n == 1:
            return ['0','1']

        lower = self.grayCodeHelper(n-1)

        retList = ['0%s'%x for x in lower]
        retList.extend(['1%s'%x for x in reversed(lower)])

        return retList

if __name__ == "__main__":
    n = int(input().strip())

    print(Solution().grayCode(n))

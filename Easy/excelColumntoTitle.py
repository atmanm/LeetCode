#Given a positive integer, return its corresponding column title as appear in an
#Excel sheet.

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        charList = []
        while n > 0:
            charNum = (n-1) % 26
            charList.append(chr(charNum+ord('A')))
            n = (n-1)//26
        return "".join(charList[::-1])

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().convertToTitle(n))

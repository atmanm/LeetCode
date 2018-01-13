#Given a column title as appear in an Excel sheet, return its corresponding
#column number.

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        num = 0
        for char in reversed(s):
            charNum = ord(char) - ord('A')
            num += (charNum+1)*(26**index)
            index += 1

        return num

if __name__ == "__main__":
    s = str(input().strip())
    print(Solution().titleToNumber(s))

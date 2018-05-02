#Given an integer, convert it to a roman numeral.

class Solution(object):

    _intStack = [(1, 'I'),
                 (4, 'IV'),
                 (5, 'V'),
                 (9, 'IX'),
                 (10, 'X'),
                 (40, 'XL'),
                 (50, 'L'),
                 (90, 'XC'),
                 (100, 'C'),
                 (400, 'CD'),
                 (500, 'D'),
                 (900, 'CM'),
                 (1000, 'M')]
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ""

        (romanNum, letter) = self._intStack.pop()
        quotient = num//romanNum
        remainder = num%romanNum

        return str((letter*quotient)+self.intToRoman(remainder))

if __name__ == "__main__":
    num = int(input().strip())
    print(Solution().intToRoman(num))

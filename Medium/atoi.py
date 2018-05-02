#Implement atoi to convert a string to an integer.

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        s = s.strip()

        sign = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        ret = 0
        for idx, char in enumerate(s):
            if char.isdigit():
                ret = 10*ret + (ord(char)-ord('0'))
            else:
                break

        return max(-2**31, min(ret*sign, 2**31-1))

if __name__ == "__main__":
    s = str(input())
    print(Solution().myAtoi(s))

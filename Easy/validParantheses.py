#Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid
#but "(]" and "([)]" are not.

class Solution(object):
    paranDict = {}
    paranDict[']'] = '['
    paranDict[')'] = '('
    paranDict['}'] = '{'
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in [']', '}', ')']:
                try:
                    openParan = stack.pop()
                except IndexError:
                    return False
                if openParan != self.paranDict[c]:
                    return False
            else:
                stack.append(c)

        if len(stack):
            return False
        return True


if __name__ == "__main__":
    string = str(input().strip())
    print(Solution().isValid(string))

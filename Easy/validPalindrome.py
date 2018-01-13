#Given a string, determine if it is a palindrome, considering only alphanumeric
#characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        return s == s[::-1]

if __name__ == "__main__":
    s = str(input().strip())
    print(Solution().isPalindrome(s))

#Given a string s, find the longest palindromic substring in s. You may assume
#that the maximum length of s is 1000.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for idx, char in enumerate(s):
            res = max(self.isPal(s, idx, idx), self.isPal(s, idx, idx+1), res, key=len)
        return res

    def isPal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l, r = l-1, r+1
        return s[l+1:r]

if __name__ == "__main__":
    s = str(input().strip())
    print(Solution().longestPalindrome(s))

#Return the index of the first occurrence of needle in haystack, or -1 if needle
#is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLen = len(needle)

        if needleLen == 0:
            return 0

        if haystack == needle:
            return 0

        haystackIdx = 0

        while haystackIdx < len(haystack) - needleLen + 1:
            if needle == haystack[haystackIdx:haystackIdx+needleLen]:
                return haystackIdx
            haystackIdx = haystackIdx + 1

        return -1

if __name__ == "__main__":
    haystack = input()
    needle = input()

    print(Solution().strStr(haystack, needle))

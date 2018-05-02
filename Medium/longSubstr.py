#Given a string, find the length of the longest substring without repeating
#characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charDict = {}
        startIdx, maxLen, repIdx = 0, 0, 0
        for idx, char in enumerate(s):
            try:
                repIdx = charDict[char]
            except KeyError:
                pass
            else:
                startIdx = max(startIdx, repIdx + 1)

            charDict[char] = idx
            maxLen = max(maxLen, (idx - startIdx + 1))

        return maxLen

if __name__ == "__main__":
    string = str(input().strip())
    print (Solution().lengthOfLongestSubstring(string))

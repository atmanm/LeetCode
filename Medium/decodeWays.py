#A message containing letters from A-Z is being encoded to corresponding numbers
#Given an encoded message containing digits, determine the total number of ways
#to decode it.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        numDict = {}
        return self.decodingHelper(s, numDict)
    def decodingHelper(self, s, numDict):
        if s in numDict.keys():
            return numDict[s]
        lower1, lower2 = 0, 0
        if len(s) == 0:
            lower1 = 1
        elif len(s) == 1:
            if self.isValidChar(s):
                lower1 = 1
            else:
                lower1 = 0
        else:
            lower1 = self.decodingHelper(s[1:], numDict)
            lower2 = self.decodingHelper(s[2:], numDict)
            if not self.isValidChar(s[0]):
                lower1 = 0
                lower2 = 0
            if not self.isValidChar(s[:2]):
                lower2 = 0

        numDict[s] = lower1 + lower2
        return lower1 + lower2

    def isValidChar(self, s):
        numInInt = int(s)

        if numInInt == 0 or numInInt > 26:
            return False

        return True

if __name__ == "__main__":
    s = str(input().strip())

    print(Solution().numDecodings(s))

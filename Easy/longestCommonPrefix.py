#Write a function to find the longest common prefix string amongst an array of
#strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        try:
            LCB = strs[0]
        except IndexError:
            return ""
        for i in range(len(LCB)):
            for string in strs[1:]:
                #Checks for ith character in each string before
                #going to next character in LCB
                if i >= len(string) or LCB[i] != string[i]:
                    return LCB[:i]
        return LCB


if __name__ == "__main__":
    strs = [str(x) for x in input().strip().split(' ')]
    if not strs:
        print()
        exit()
    print (Solution().longestCommonPrefix(strs))


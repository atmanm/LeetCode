#Given an array of strings, group anagrams together.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramDict = {}

        for string in strs:
            sortedString = ''.join(sorted(string))
            try:
                anagramDict[sortedString].append(string)
            except KeyError:
                anagramDict[sortedString] = [string]

        return list(anagramDict.values())

if __name__ == "__main__":
    strs = [str(x) for x in input().strip().split(',')]
    print(Solution().groupAnagrams(strs))

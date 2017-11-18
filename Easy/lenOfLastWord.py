#Given a string s consists of upper/lower-case alphabets and empty space
#characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.
#Note: A word is defined as a character sequence consists of non-space characters
#only.

class Solution(object):
    def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    wordList = [x for x in s.split(' ') if x != '']
    if len(wordList) == 0:
        return 0
    else:
        return len(wordList[-1])

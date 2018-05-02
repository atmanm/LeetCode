#Given a digit string, return all possible letter combinations that the number
#could represent.
#A mapping of digit to letters is just like on the telephone buttons

class Solution(object):
    letterDict = {
            '1': "",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
            }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        retList = []
        curNumber = digits[0]
        curGenerator = self.myGenerator(self.letterDict[curNumber])
        for letter in curGenerator:
            curList = self.letterCombinations(digits[1:])
            if len(curList) == 0:
                retList.append(letter)
            else:
                retList.extend([letter+x for x in curList])

        return retList

    def myGenerator(self, letterCom):
        for i in letterCom:
            yield i

if __name__ == "__main__":
    digits = str(input().strip())
    print (Solution().letterCombinations(digits))

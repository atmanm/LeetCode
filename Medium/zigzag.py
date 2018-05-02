#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
#rows like this:
#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number
#of rows

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if len(s) <= numRows or numRows == 1:
            return s
#        #Don't bother understanding below. Draw the above example for numRows =
#        #3, 4, 5, 6 and derive the formula
#        curStr = ''
#        for i in range(numRows):
#            curDiff = [numRows - i - 1, i]
#            idx, diffFlag = i, 1
#            while idx < len(s):
#                diffFlag = 1 - diffFlag
#                if curDiff[diffFlag]:
#                    curStr += ''.join(s[idx])
#                    idx += 2*curDiff[diffFlag]
#
#        return curStr

        L = ['']*numRows
        index, step = 0,1

        for char in s:
            L[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)


if __name__ == "__main__":
    s = str(input().strip())
    numRows = int(input().strip())

    print (Solution().convert(s, numRows))

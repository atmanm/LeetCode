#Given numRows, generate the first numRows of Pascal's triangle.

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        retList = []
        prevList = []
        for i in range(numRows):
            curList = [1]
            index = 0
            while index < i:
                try:
                    curNum = prevList[index] + prevList[index+1]
                except IndexError:
                    curNum = 1
                curList.append(curNum)
                index += 1
            prevList = curList
            retList.append(curList)

        return retList

if __name__ == "__main__":
    numRows = int(input().strip())
    print(Solution().generate(numRows))

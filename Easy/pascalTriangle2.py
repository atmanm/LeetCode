#Given an index k, return the kth row of the Pascal's triangle.
#For example, given k = 3,
#Return [1,3,3,1].
#Note: Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        curList = [1]
        for i in range(rowIndex):
            curList = [x+y for x,y in zip([0]+curList, curList+[0])]
            #index = 0
            #curList.insert(0,0)
            #while index < i+1:
            #    curList[index] = (curList[index] + curList[index + 1])
            #    index += 1

        return curList

if __name__ == "__main__":
    rowIndex = int(input().strip())
    print(Solution().getRow(rowIndex))

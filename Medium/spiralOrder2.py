#Given an integer n, generate a square matrix filled with elements from 1 to n2
#in spiral order.

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        retMatrix = [[0]*n for _ in range(n)]

        self.generateHelper(n, retMatrix, n)

        return retMatrix

    def generateHelper(self, n, matrix, maxN):
        if n != 0:
            if n < 2:
                matrix[maxN//2][maxN//2] = maxN**2
            else:
                self.generateHelper(n-2, matrix, maxN)
                numEntries = n**2 - ((n-2)**2)
                startNum = maxN**2 - n**2 + 1
                topRow = [startNum+i for i in range(n)]
                matrix[(maxN-n)//2][(maxN-n)//2:(maxN+n)//2] = topRow
                bottomStart = maxN**2 - ((n-1)**2)
                bottomRow = [bottomStart+i for i in range(n)]
                matrix[(maxN+n)//2-1][(maxN-n)//2:(maxN+n)//2] = bottomRow[::-1]
                rightStart = bottomStart - n + 1
                rightCol = [rightStart + 1 + i for i in range(n-2)]
                if rightCol:
                    startIdx = (maxN-n)//2+1
                    for i in range(len(rightCol)):
                        matrix[startIdx][(maxN+n)//2-1] = rightCol[i]
                        startIdx += 1
                leftStart = bottomStart + n
                leftCol = [leftStart + i for i in range(n-2)]
                if leftCol:
                    startIdx = (maxN-n)//2+1
                    for i in range(len(leftCol)):
                        matrix[startIdx][(maxN-n)//2] = leftCol[-i-1]
                        startIdx += 1

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().generateMatrix(n))

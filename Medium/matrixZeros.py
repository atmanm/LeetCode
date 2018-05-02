# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify
        matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        mBitArray = 0
        nBitArray = 0

        for i, row in enumerate(matrix):
            for j, elem in enumerate(matrix[i]):
                if elem == 0:
                    mBitArray |= 1<<i
                    nBitArray |= 1<<j

        rowIdx = 0
        while mBitArray:
            if mBitArray & 1:
                matrix[rowIdx] = [0]*n
            mBitArray >>= 1
            rowIdx += 1

        colIdx = 0
        while nBitArray:
            if nBitArray & 1:
                for i in range(m):
                    matrix[i][colIdx] = 0
            nBitArray >>= 1
            colIdx += 1

if __name__ == "__main__":
    inputMatrix = str(input())
    matrix = eval(inputMatrix)

    Solution().setZeroes(matrix)

    print(matrix)

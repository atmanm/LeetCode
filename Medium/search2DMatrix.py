#Write an efficient algorithm that searches for a value in an m x n matrix. This
#matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        rowIdx = -1
        start = 0
        end = m - 1

        while start <= end:
            mid = (start+end)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                if target <= matrix[mid][-1]:
                    rowIdx = mid
                    break
                else:
                    start = mid + 1

        if rowIdx == -1:
            return False

        start = 0
        end = n - 1

        while start <= end:
            mid = (start+end)//2
            if matrix[rowIdx][mid] == target:
                return True
            elif matrix[rowIdx][mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

if __name__ == "__main__":
    inputMatrix = str(input().strip())
    target = int(input().strip())

    matrix = eval(inputMatrix)

    print(Solution().searchMatrix(matrix, target))

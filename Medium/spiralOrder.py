#Given a matrix of m x n elements (m rows, n columns), return all elements of
#the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            result.extend(matrix[0])
            matrix.pop(0)

            if matrix and matrix[0]:
                [result.extend([x[-1]]) for x in matrix]
                [x.pop(-1) for x in matrix]

            if matrix:
                result.extend(matrix[-1][::-1])
                matrix.pop(-1)

            if matrix and matrix[0]:
                leftCol = [x.pop(0) for x in matrix]
                result.extend(leftCol[::-1])
        return result

if __name__ == "__main__":
    board = input().strip()
    matrix = eval(board)
    print(Solution().spiralOrder(matrix))

#You are given an n x n 2D matrix representing an image.
#Rotate the image by 90 degrees (clockwise).
#Note:
#You have to rotate the image in-place, which means you have to modify the
#input 2D matrix directly. DO NOT allocate another 2D matrix and do the
#rotation.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify
        matrix in-place instead.
        """
        matrix = self.rotateHelper(matrix)
        print(matrix)
        return 0

    def rotateHelper(self, matrix):
        if matrix:
            length = len(matrix[0])
            for i in range(length-1):
                matrix[0][i],\
                matrix[i][length-1],\
                matrix[length-1][length-1-i],\
                matrix[length-1-i][0] = \
                matrix[length-1-i][0],\
                matrix[0][i],\
                matrix[i][length-1],\
                matrix[length-1][length-1-i]
            newMatrix = matrix[1:-1]
            newMatrix = [x[1:-1] for x in newMatrix]
            rotMatrix = self.rotateHelper(newMatrix)
            if rotMatrix:
                for index,myList in enumerate(rotMatrix):
                    matrix[index+1][1:-1] = myList
        return matrix

if __name__ == "__main__":
    image = input().strip()
    matrix = eval(image)
    Solution().rotate(matrix)

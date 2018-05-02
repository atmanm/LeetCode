#A robot is located at the top-left corner of a m x n grid.
#The robot can only move either down or right at any point in time. The robot is
#trying to reach the bottom-right corner of the grid
#How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        pathArray = [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                pathArray[i][j] = pathArray[i-1][j] + pathArray[i][j-1]

        return pathArray[-1][-1]

if __name__ == "__main__":
    m = int(input().strip())
    n = int(input().strip())

    print(Solution().uniquePaths(m, n))

#Follow up for "Unique Paths":
#Now consider if some obstacles are added to the grids. How many unique paths
#would there be?
#An obstacle and empty space is marked as 1 and 0 respectively in the grid.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        pathArray = [[1 for x in row] for row in obstacleGrid]

        pathArray[0][0] = 1 - obstacleGrid[0][0]

        for i in range(len(pathArray)):
            if obstacleGrid[i][0]:
                pathArray[i][0] = 0
            else:
                pathArray[i][0] = pathArray[i-1][0]

        for i in range(len(pathArray[0])):
            if obstacleGrid[0][i]:
                pathArray[0][i] = 0
            else:
                pathArray[0][i] = pathArray[0][i-1]

        for i in range(1, len(pathArray)):
            for j in range(1, len(pathArray[0])):
                if obstacleGrid[i][j] == 0:
                    pathArray[i][j] = pathArray[i-1][j] + pathArray[i][j-1]
                else:
                    pathArray[i][j] = 0

        return pathArray[-1][-1]

if __name__ == "__main__":
    obstacles = str(input().strip())
    obstacleGrid = eval(obstacles)

    print(Solution().uniquePathsWithObstacles(obstacleGrid))

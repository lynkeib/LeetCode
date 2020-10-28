class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        if not rows:
            return 0
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1
        ## init row[0]
        for col in range(1, cols):
            if obstacleGrid[0][col] != 1:
                dp[0][col] = dp[0][col - 1]
        ## init col[0]
        for row in range(1, rows):
            if obstacleGrid[row][0] != 1:
                dp[row][0] = dp[row - 1][0]
        ## loop
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[rows - 1][cols - 1]
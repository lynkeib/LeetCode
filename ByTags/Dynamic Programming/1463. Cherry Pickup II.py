class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[[0 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        for row in range(rows - 1, -1, -1):
            for col1 in range(cols):
                for col2 in range(cols):
                    res = 0
                    res += grid[row][col1]
                    if col1 != col2:
                        res += grid[row][col2]

                    if row != rows - 1:
                        prev_max = 0
                        for new_col1 in [col1, col1 + 1, col1 - 1]:
                            for new_col2 in [col2, col2 + 1, col2 - 1]:
                                if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                                    prev_max = max(prev_max, dp[row + 1][new_col1][new_col2])
                        res += prev_max
                    dp[row][col1][col2] = res
        return dp[0][0][cols - 1]
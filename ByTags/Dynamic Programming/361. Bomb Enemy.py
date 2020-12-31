class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        res = 0
        if rows == 0:
            return res
        cols = len(grid[0])

        row_hit, col_hit = 0, [0] * cols

        for row in range(rows):
            for col in range(cols):
                # count row hit
                if col == 0 or grid[row][col - 1] == 'W':
                    row_hit = 0
                    for k in range(col, cols):
                        if grid[row][k] == 'W':
                            break
                        elif grid[row][k] == 'E':
                            row_hit += 1
                # count col hit
                if row == 0 or grid[row - 1][col] == 'W':
                    col_hit[col] = 0
                    for k in range(row, rows):
                        if grid[k][col] == 'W':
                            break
                        elif grid[k][col] == 'E':
                            col_hit[col] += 1

                if grid[row][col] == '0':
                    total = row_hit + col_hit[col]
                    res = max(res, total)
        return res

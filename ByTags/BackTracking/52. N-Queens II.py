class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        hasQ = [-1] * n
        res = [0]
        self.dfs(n, hasQ, 0, res)
        return res[0]

    def dfs(self, n, hasQ, row, res):
        if row == n:
            res[0] += 1
            return

        cannot = [0 for _ in range(n)]
        for r in range(row):
            col = hasQ[r]
            if col != -1:
                cannot[col] = 1
            diff = row - r
            if col + diff < n:
                cannot[col + diff] = 1
            if col - diff > -1:
                cannot[col - diff] = 1

        if sum(cannot) == n:
            return

        for c in range(n):
            if cannot[c] == 0:
                hasQ[row] = c
                self.dfs(n, hasQ, row + 1, res)
                hasQ[row] = -1

        return
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        L = len(s)
        dp = [[0 for _ in range(L)] for _ in range(L)]
        res = []
        self.dfs(s, 0, [], dp, res)
        return res

    def dfs(self, s, start, path, dp, res):
        if start >= len(s):
            res.append(path[:])
            return
        for end in range(start, len(s)):
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = 1
                path.append(s[start:end + 1])
                self.dfs(s, end + 1, path, dp, res)
                path.pop()
        return

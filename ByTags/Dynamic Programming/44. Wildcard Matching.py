class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]

        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = False
        for indexs in range(1, len(s) + 1):
            for indexp in range(1, len(p) + 1):
                res = False
                if p[indexp - 1] == "*":
                    res = dp[indexp - 1][indexs - 1] or dp[indexp - 1][indexs] or dp[indexp][indexs - 1]
                elif p[indexp - 1] == "?":
                    res = dp[indexp - 1][indexs - 1]
                else:
                    res = dp[indexp - 1][indexs - 1] and (s[indexs - 1] == p[indexp - 1])
                dp[indexp][indexs] = res
        return dp[len(p)][len(s)]
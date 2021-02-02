class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dp = [-1 for _ in range(len(S))]
        # init
        for i in range(len(S)):
            if S[i] == T[0]:
                dp[i] = i

        for j in range(1, len(T)):
            prev = -1
            new_dp = [-1 for _ in range(len(S))]
            for i in range(len(S)):
                if prev != -1 and S[i] == T[j]:
                    new_dp[i] = prev
                if dp[i] != -1:
                    prev = dp[i]
            dp = new_dp
        res = float("inf")
        res_str = ""
        for i in range(len(dp)):
            if dp[i] >= 0 and i - dp[i] + 1 >= len(T):
                length = i - dp[i] + 1
                if length < res:
                    res = length
                    res_str = S[dp[i]:i + 1]
        # for i in range(len(dp)):
        #     print(dp[i], i)
        return res_str

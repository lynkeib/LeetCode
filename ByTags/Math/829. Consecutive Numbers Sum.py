class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1

        upper = int(ceil((2 * N + 0.25) ** 0.5 - 0.5)) + 1
        res = 0

        for k in range(1, upper):
            if (N - k * (k + 1) // 2) % k == 0:
                res += 1

        return res
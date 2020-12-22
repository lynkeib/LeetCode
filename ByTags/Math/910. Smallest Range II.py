class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        Min, Max = A[0], A[-1]
        res = Max - Min
        for i in range(len(A) - 1):
            smaller, bigger = A[i], A[i + 1]
            thisMin, thisMax = min(Min + K, bigger - K), max(Max - K, smaller + K)
            res = min(res, thisMax - thisMin)
        return res
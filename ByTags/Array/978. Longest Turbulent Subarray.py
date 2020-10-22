class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 1
        slow = 0
        for fast in range(1, len(A)):
            currDiff = A[fast] - A[fast - 1]
            if currDiff == 0:
                slow = fast
            elif fast == len(A) - 1 or currDiff * (A[fast + 1] - A[fast]) >= 0:
                res = max(res, fast - slow + 1)
                slow = fast
        return res
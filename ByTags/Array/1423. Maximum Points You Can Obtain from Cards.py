class Solution(object):
    res = 0

    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) <= k:
            return sum(cardPoints)

        currSum = 0
        size = len(cardPoints) - k
        Min = float("inf")
        left = 0
        for right in range(len(cardPoints)):
            currSum += cardPoints[right]
            if right - left + 1 > size:
                currSum -= cardPoints[left]
                left += 1
            if right - left + 1 == size:
                Min = min(Min, currSum)
        return sum(cardPoints) - Min


# DFS, TLE

class Solution(object):
    res = 0

    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) <= k:
            return sum(cardPoints)
        self.dfs(0, len(cardPoints) - 1, cardPoints, k, 0)
        return self.res

    def dfs(self, index_left, index_right, cardPoints, k, s):
        if self.steps(index_left, index_right, len(cardPoints)) == k:
            self.res = max(self.res, s)
            return
        self.dfs(index_left + 1, index_right, cardPoints, k, s + cardPoints[index_left])
        self.dfs(index_left, index_right - 1, cardPoints, k, s + cardPoints[index_right])
        return

    def steps(self, index_left, index_right, length):
        return (index_left) + (length - index_right - 1)

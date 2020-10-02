class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res = 0
        minV, maxV = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            thisMin, thisMax = arrays[i][0], arrays[i][-1]
            res = max(res, abs(maxV - thisMin), abs(thisMax - minV))
            maxV = max(maxV, thisMax)
            minV = min(minV, thisMin)
        return res
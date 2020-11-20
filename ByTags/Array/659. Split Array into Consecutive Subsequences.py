class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        fMap = collections.defaultdict(int)
        hMap = collections.defaultdict(int)

        for n in nums:
            fMap[n] += 1

        for n in nums:
            if fMap[n] == 0:
                continue
            if hMap[n] > 0:
                fMap[n] -= 1
                hMap[n] -= 1
                hMap[n + 1] += 1
            elif fMap[n] > 0 and fMap[n + 1] > 0 and fMap[n + 2] > 0:
                fMap[n] -= 1
                fMap[n + 1] -= 1
                fMap[n + 2] -= 1
                hMap[n + 3] += 1
            else:
                return False

        return True
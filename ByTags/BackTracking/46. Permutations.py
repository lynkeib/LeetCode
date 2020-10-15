class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backTracking(nums, 0, res)
        return res

    def backTracking(self, nums, index, res):
        if index == len(nums):
            res.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.backTracking(nums, index + 1, res)
            nums[i], nums[index] = nums[index], nums[i]
        return
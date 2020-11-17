class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            slow, fast = i, self.getIndex(i, nums)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[self.getIndex(fast, nums)] > 0:
                if slow == fast:
                    if fast == self.getIndex(fast, nums):
                        break
                    return True
                slow = self.getIndex(slow, nums)
                fast = self.getIndex(self.getIndex(fast, nums), nums)
            slow = i
            thisVal = nums[slow]
            while nums[slow] * thisVal > 0:
                nextSlow = self.getIndex(slow, nums)
                nums[slow] = 0
                slow = nextSlow
        return False

    def getIndex(self, index, nums):
        return (index + nums[index]) % len(nums)

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.length = len(nums)
        self.Map = dict()
        for i in range(self.length):
            if nums[i] != 0:
                self.Map[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for i in range(self.length):
            if i in self.Map and i in vec.Map:
                res += self.Map[i] * vec.Map[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
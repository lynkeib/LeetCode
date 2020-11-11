class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1n2 = 0
        num1 = 0
        num2 = 0

        for n in nums:
            n1n2 ^= n

        rightMost = 1
        while rightMost & n1n2 == 0:
            rightMost <<= 1

        for n in nums:
            if n & rightMost == 0:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]
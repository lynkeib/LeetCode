class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = 1 if x >= 0 else -1
        x = abs(x)
        intMax, intMin = 2**31 - 1, -2**31
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        res *= flag
        if res <= intMin or res >=intMax:
            return 0
        return res
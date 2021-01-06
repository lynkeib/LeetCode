class Solution(object):
    count = 0

    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.count = k
        res = self.backtracking("", n)
        return res if res else ""

    def backtracking(self, string, n):
        if len(string) == n:
            self.count -= 1
            if self.count == 0:
                return string
            return False
        for c in ("a", "b", "c"):
            if not string or string[-1] != c:
                res = self.backtracking(string + c, n)
                if res:
                    return res
        return False

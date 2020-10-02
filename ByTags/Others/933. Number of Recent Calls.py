class RecentCounter(object):

    def __init__(self):
        self.slow = 0
        self.l = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.l.append(t)
        while self.slow < len(self.l) and self.l[self.slow] < t - 3000:
            self.slow += 1
        return len(self.l) - self.slow


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
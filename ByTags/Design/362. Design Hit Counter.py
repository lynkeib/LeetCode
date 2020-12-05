class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0, i + 1] for i in range(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        index = (timestamp - 1) % 300
        if self.counter[index][1] == timestamp:
            self.counter[index][0] += 1
        else:
            self.counter[index][0] = 1
            self.counter[index][1] = timestamp

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for x in self.counter:
            hits, time = x[0], x[1]
            if timestamp - time < 300:
                res += hits
        return res

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
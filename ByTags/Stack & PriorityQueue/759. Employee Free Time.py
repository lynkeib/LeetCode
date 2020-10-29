"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        res = []
        heap = []
        for index, item in enumerate(schedule):
            heapq.heappush(heap, (item[0].start, index, 0))

        currStart = heap[0][0]

        while heap:
            curr, index, currIndex = heapq.heappop(heap)
            if curr > currStart:
                res.append(Interval(currStart, curr))
            currStart = max(currStart, schedule[index][currIndex].end)
            if currIndex + 1 < len(schedule[index]):
                currIndex += 1
                heapq.heappush(heap, (schedule[index][currIndex].start, index, currIndex))
        return res


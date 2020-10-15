class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        queue = intervals
        res = []
        while queue:
            item = queue.pop(0)
            if item[0] <= newInterval[0] and item[1] >= newInterval[0]:
                newInterval[0] = min(item[0],  newInterval[0])
                newInterval[1] = max(item[1],  newInterval[1])
            elif newInterval[1] >= item[0] and newInterval[0] <= item[0]:
                newInterval[0] = min(item[0],  newInterval[0])
                newInterval[1] = max(item[1],  newInterval[1])
            else:
                if item[1] < newInterval[0]:
                    res.append(item)
                else:
                    res.append(newInterval)
                    newInterval = item
        res.append(newInterval)
        return res
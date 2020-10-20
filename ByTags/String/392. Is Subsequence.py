
# linear
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        indexs, indext = 0, 0
        while indexs < len(s) and indext < len(t):
            if s[indexs] == t[indext]:
                indexs+= 1
            indext += 1
        return indexs == len(s)

# binary search when having too many s
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Map = collections.defaultdict(list)
        for i, c in enumerate(t):
            Map[c].append(i)

        currIndex = -1

        for c in s:
            if c not in Map:
                return False
            thisIndex = self.bisect_right(Map[c], currIndex)
            if thisIndex == len(Map[c]):
                return False
            currIndex = Map[c][thisIndex]
        return True

    def bisect_right(self, lst, index):
        left, right = 0, len(lst) - 1
        while left < right:
            mid = left + (right - left) // 2
            if lst[mid] <= index:
                left = mid + 1
            else:
                right = mid
        if lst[left] <= index:
            left += 1
        return left

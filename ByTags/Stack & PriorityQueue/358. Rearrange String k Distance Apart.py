class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        counter = [0 for _ in range(26)]
        for c in s:
            counter[ord(c) - ord('a')] += 1
        heap = []
        for i in range(26):
            if counter[i] != 0:
                heapq.heappush(heap, (-counter[i], chr(i + ord('a'))))
        added = set()
        res = ""
        temp_heap = []
        while heap or temp_heap:
            if len(temp_heap) >= k:
                for h in temp_heap:
                    if h[0] != 0:
                        heapq.heappush(heap, h)
                temp_heap = []
            if len(res) == len(s):
                return res

            if not heap:
                return ""
            t = heapq.heappop(heap)
            res += t[1]
            temp_heap.append((t[0] + 1, t[1]))
            # print(res, heap, temp_heap)
        return res



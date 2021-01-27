class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        Map = dict()
        for a, b, n in transactions:
            if a not in Map:
                Map[a] = 0
            if b not in Map:
                Map[b] = 0
            Map[a] += n
            Map[b] -= n

        lst = []
        for k, v in Map.items():
            if v != 0:
                lst.append(v)
        return self.dfs(0, lst)

    def dfs(self, k, lst):
        if k == len(lst):
            return 0
        curr = lst[k]
        if curr == 0:
            return self.dfs(k + 1, lst)
        Min = float("inf")
        for i in range(k + 1, len(lst)):
            n = lst[i]
            if curr * n < 0:
                lst[i] = curr + n
                Min = min(Min, 1 + self.dfs(k + 1, lst))
                lst[i] = n
                if curr + n == 0:
                    break
        return Min
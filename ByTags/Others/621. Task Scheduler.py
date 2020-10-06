class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        f = [0] * 26
        for t in tasks:
            f[ord(t) - ord("A")] += 1

        f_max = max(f)
        n_max = f.count(f_max)
        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord("a")].append(it)

        for c in S:
            c_index = ord(c) - ord("a")
            old = heads[c_index]
            heads[c_index] = []

            while old:
                it = old.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord("a")].append(it)
                else:
                    res += 1
        return res
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs or len(seqs) == 0:
            return False
        pairs = [0 for _ in range(len(org))]
        indexDict = dict()
        for index, value in enumerate(org):
            indexDict[value] = index

        for seq in seqs:
            for index in range(len(seq)):
                if seq[index] not in indexDict:
                    return False
                if index > 0 and indexDict[seq[index - 1]] >= indexDict[seq[index]]:
                    return False
                if index > 0 and indexDict[seq[index - 1]] + 1 == indexDict[seq[index]]:
                    i = indexDict[seq[index - 1]]
                    pairs[i] = 1
        for i in range(len(org) - 1):
            if pairs[i] != 1:
                return False
        return True


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:

        # edge case
        if not seqs: return False

        # a. Initialize the graph and indegree
        Graph = {}
        inDegree = {}
        for sequence in seqs:
            for i in sequence:
                inDegree[i] = 0
                Graph[i] = []

        # b. Build the graph and indegree
        for sequece in seqs:
            for i in range(1, len(sequece)):
                parent, child = sequece[i - 1], sequece[i]
                Graph[parent].append(child)
                inDegree[child] += 1

        if len(inDegree) != len(org): return False

        # c. Find the source of the sequence
        source = collections.deque()
        for i in inDegree:
            if inDegree[i] == 0:
                source.append(i)

        # d. Topological sorting for the calculation
        res = []
        while source:
            max_len = len(source)
            if max_len > 1:
                return False
            if org[len(res)] != source[0]:
                return False
            vertext = source.popleft()
            res.append(vertext)
            for child in Graph[vertext]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    source.append(child)

        return len(res) == len(org)
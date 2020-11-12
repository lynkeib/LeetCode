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
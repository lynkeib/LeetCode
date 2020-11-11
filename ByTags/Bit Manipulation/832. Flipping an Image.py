class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in range(len(A)):
            left, right = 0, len(A[0]) - 1
            while left <= right:
                A[row][left], A[row][right] = A[row][right] ^ 1, A[row][left] ^ 1
                left += 1
                right -= 1
        return A
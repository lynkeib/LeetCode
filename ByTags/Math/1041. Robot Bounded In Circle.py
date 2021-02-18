class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
        x = y = index = 0
        for c in instructions:
            if c == "L":
                index = (index + 3) % 4
            elif c == "R":
                index = (index + 1) % 4
            else:
                x += dirs[index][1]
                y += dirs[index][0]
        return index != 0 or (x == 0 and y == 0)

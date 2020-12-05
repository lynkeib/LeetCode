class Solution(object):
    dirs = [
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1)
    ]

    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = abs(x), abs(y)
        queue = [[0, 0]]
        res = 0
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                cx, cy = queue.pop(0)
                if cx == x and cy == y:
                    return res
                if cx >= -1 and cy >= -1:
                    for dx, dy in self.dirs:
                        nx, ny = cx + dx, cy + dy
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append([nx, ny])
            res += 1
        return -1

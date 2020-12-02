class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        rows, cols = len(maze), len(maze[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        return self.dfs(maze, start[0], start[1], destination[0], destination[1], visited)

    def dfs(self, maze, curr_row, curr_col, dest_row, dest_col, visited):

        if visited[curr_row][curr_col]:
            return False

        if curr_row == dest_row and curr_col == dest_col:
            return True
        visited[curr_row][curr_col] = 1

        # go up
        up = curr_row
        while up > -1 and maze[up][curr_col] == 0:
            up -= 1
        if self.dfs(maze, up + 1, curr_col, dest_row, dest_col, visited):
            return True

        # go down
        down = curr_row
        while down < len(maze) and maze[down][curr_col] == 0:
            down += 1
        if self.dfs(maze, down - 1, curr_col, dest_row, dest_col, visited):
            return True

        # go left
        left = curr_col
        while left > -1 and maze[curr_row][left] == 0:
            left -= 1
        if self.dfs(maze, curr_row, left + 1, dest_row, dest_col, visited):
            return True

        # go right
        right = curr_col
        while right < len(maze[0]) and maze[curr_row][right] == 0:
            right += 1
        if self.dfs(maze, curr_row, right - 1, dest_row, dest_col, visited):
            return True

        return False

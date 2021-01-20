# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtracking(x, y, d):
            visited.add((x, y))
            robot.clean()

            for k in range(4):
                new_d = (d + k) % 4
                new_x = x + dirs[new_d][0]
                new_y = y + dirs[new_d][1]

                if (new_x, new_y) not in visited and robot.move():
                    backtracking(new_x, new_y, new_d)
                    go_back()
                robot.turnRight()

        visited = set([])
        backtracking(0, 0, 0)

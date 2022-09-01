#
# @lc app=leetcode.cn id=463 lang=python
#
# [463] 岛屿的周长
#


# @lc code=start
class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(grid, row, col):
            if not (0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])):
                # out of range
                return 1
            if grid[row][col] == 0:
                # not island
                return 1
            if grid[row][col] == 2:
                # skip traversaled
                return 0
            # mark traversaled
            grid[row][col] = 2
            return dfs(grid, row - 1, col) + \
                    dfs(grid, row + 1, col) + \
                    dfs(grid, row, col - 1) + \
                    dfs(grid, row, col + 1)  # up down left right

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(grid, row, col)
        return 0

# @lc code=end

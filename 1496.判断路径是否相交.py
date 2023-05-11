#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#


# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirs = {
            "N": (-1, 0),
            "S": (1, 0),
            "W": (0, -1),
            "E": (0, 1),
        }

        x, y = 0, 0
        vis = set([(x, y)])
        for ch in path:
            dx, dy = dirs[ch]
            x, y = x + dx, y + dy
            if (x, y) in vis:
                return True
            vis.add((x, y))

        return False


# @lc code=end

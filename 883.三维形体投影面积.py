#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        zxArea = sum(map(max, grid))
        return xyArea + yzArea + zxArea

# @lc code=end


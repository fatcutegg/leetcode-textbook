#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5 * abs(xa*yb + xb*yc + xc*ya - xb*ya - xc*yb - xa*yc)
                   for (xa, ya), (xb, yb), (xc, yc) in itertools.combinations(points, 3))
# @lc code=end


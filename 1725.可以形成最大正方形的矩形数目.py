#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#


# @lc code=start
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l = [min(x[0], x[1]) for x in rectangles]
        return l.count(max(l))


# @lc code=end

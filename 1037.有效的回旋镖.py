#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points.sort()
        return (points[2][0]-points[1][0]) * (points[1][1]-points[0][1]) != (points[1][0]-points[0][0]) * (points[2][1]-points[1][1]) 
# @lc code=end


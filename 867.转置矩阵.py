#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(list(row) for row in zip(*matrix))
# @lc code=end


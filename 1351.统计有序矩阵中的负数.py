#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#


# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for item in grid:
            for num in item:
                if num < 0:
                    total += 1

        return total


# @lc code=end

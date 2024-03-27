#
# @lc app=leetcode.cn id=2894 lang=python3
#
# [2894] 分类求和并作差
#


# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n + 1) // 2 - n // m * (n // m + 1) * m


# @lc code=end

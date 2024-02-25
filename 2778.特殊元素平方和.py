#
# @lc app=leetcode.cn id=2778 lang=python3
#
# [2778] 特殊元素平方和
#

# @lc code=start
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(x * x for i, x in enumerate(nums, 1) if len(nums) % i == 0)


# @lc code=end

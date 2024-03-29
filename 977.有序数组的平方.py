#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)

# @lc code=end


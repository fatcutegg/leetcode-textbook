#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sorted(nums) == nums or sorted(nums,reverse=True) == nums
# @lc code=end


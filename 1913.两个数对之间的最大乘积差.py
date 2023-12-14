#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#


# @lc code=start
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


# @lc code=end

#
# @lc app=leetcode.cn id=2574 lang=python3
#
# [2574] 左右元素和的差值
#


# @lc code=start
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        for i, x in enumerate(nums):
            right_sum -= x
            nums[i] = abs(left_sum - right_sum)
            left_sum += x
        return nums


# @lc code=end

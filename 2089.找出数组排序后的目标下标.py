#
# @lc app=leetcode.cn id=2089 lang=python3
#
# [2089] 找出数组排序后的目标下标
#


# @lc code=start
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s = sorted(nums)
        return [index for index, value in enumerate(s) if value == target]


# @lc code=end

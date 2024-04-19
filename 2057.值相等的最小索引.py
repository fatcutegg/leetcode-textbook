#
# @lc app=leetcode.cn id=2057 lang=python3
#
# [2057] 值相等的最小索引
#

# @lc code=start
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        l = len(nums)
        ls = [i for i in range(l) if i % 10 == nums[i]]
        if len(ls) > 0:
            return min(ls)
        return -1


# @lc code=end

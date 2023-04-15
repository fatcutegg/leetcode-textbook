#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        tot, s = sum(nums), 0
        for i, x in enumerate(nums):
            s += x
            if s > tot - s:
                return nums[:i + 1]


# @lc code=end

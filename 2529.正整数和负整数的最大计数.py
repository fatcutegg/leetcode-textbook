#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#

# @lc code=start
from bisect import bisect_right
from typing import List

bisect_right
class Solution:

    def maximumCount(self, nums: List[int]) -> int:
        less = great = 0
        for x in nums:
            if x < 0:
                less += 1
            elif x > 0:
                great += 1
        return max(less, great)


# @lc code=end

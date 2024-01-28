#
# @lc app=leetcode.cn id=2154 lang=python3
#
# [2154] 将找到的值乘以 2
#

# @lc code=start
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for num in nums:
            if num == original:
                original *= 2
        return original


# @lc code=end

#
# @lc app=leetcode.cn id=2148 lang=python3
#
# [2148] 元素计数
#


# @lc code=start
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        res = 0
        for num in nums:
            if smallest < num < largest:
                res += 1
        return res


# @lc code=end

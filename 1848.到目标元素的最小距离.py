#
# @lc app=leetcode.cn id=1848 lang=python3
#
# [1848] 到目标元素的最小距离
#


# @lc code=start
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))
        return res


# @lc code=end

#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        for i, ch in enumerate(nums):
            if sum(nums[:i]) == sum(nums[i + 1 : n]):
                return i
        return -1


# @lc code=end

#
# @lc app=leetcode.cn id=2395 lang=python3
#
# [2395] 和相等的子数组
#


# @lc code=start
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(n - 1):
            total = nums[i] + nums[i + 1]
            if total in seen:
                return True
            seen.add(total)
        return False


# @lc code=end

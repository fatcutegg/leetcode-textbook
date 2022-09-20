#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), (1 + len(nums)) * len(nums) // 2 - sum(set(nums))]


# @lc code=end

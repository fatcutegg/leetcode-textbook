#
# @lc app=leetcode.cn id=1929 lang=python3
#
# [1929] 数组串联
#

# @lc code=start
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


# @lc code=end

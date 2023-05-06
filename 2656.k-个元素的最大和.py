#
# @lc app=leetcode.cn id=2656 lang=python3
#
# [2656] K 个元素的最大和
#

# @lc code=start
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (max(nums) * 2 + k - 1) * k // 2


# @lc code=end

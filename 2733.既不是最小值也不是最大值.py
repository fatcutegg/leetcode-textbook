#
# @lc app=leetcode.cn id=2733 lang=python3
#
# [2733] 既不是最小值也不是最大值
#

# @lc code=start
from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return sorted(nums[:3])[1] if len(nums) > 2 else -1


# @lc code=end


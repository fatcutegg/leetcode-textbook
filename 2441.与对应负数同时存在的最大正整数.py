#
# @lc app=leetcode.cn id=2441 lang=python3
#
# [2441] 与对应负数同时存在的最大正整数
#

# @lc code=start
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        for i in nums:
            if -i in seen:
                ans = max(abs(i), ans)
            seen.add(i)
        return ans
# @lc code=end


#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#


# @lc code=start
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans


# @lc code=end

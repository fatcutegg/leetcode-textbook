#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res, begin = 0, 0
        for end in range(len(nums)):
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                res = max(res, end - begin + 1)
        return res

# @lc code=end


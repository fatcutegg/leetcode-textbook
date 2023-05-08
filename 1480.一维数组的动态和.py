#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(sum(nums[:i+1]))
        return ans


# @lc code=end

#
# @lc app=leetcode.cn id=2460 lang=python3
#
# [2460] 对数组执行操作
#

# @lc code=start
from typing import List


class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        for i in range(0, n):
            for j in range(i, n):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        return nums


# @lc code=end

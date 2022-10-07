#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
from typing import List


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sums = 0
        for i in range(len(nums)):
            if 2 * sums + nums[i] == total:
                return i
            sums += nums[i]
        return -1


# @lc code=end

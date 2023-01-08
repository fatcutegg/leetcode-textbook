#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
from typing import List


class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True) # 将nums按绝对值从大到小排列
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k > 0:
            nums[-1] *= (-1)**k #取nums最后一个数只需要写-1
        return sum(nums)


# @lc code=end

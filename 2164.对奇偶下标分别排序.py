#
# @lc app=leetcode.cn id=2164 lang=python3
#
# [2164] 对奇偶下标分别排序
#

# @lc code=start
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2])
        odd = sorted(nums[1::2])[::-1]
        nums[::2] = even
        nums[1::2] = odd
        return nums


# @lc code=end

#
# @lc app=leetcode.cn id=2475 lang=python3
#
# [2475] 数组中不等三元组的数目
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:

    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        ans = start = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                ans += start * (i - start + 1) * (len(nums) - 1 - i)
                start = i + 1
        return ans


# @lc code=end

nums = [1, 2, 2, 2, 3, 4, 5, 6, 7]
Solution().unequalTriplets(nums=nums)

#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#


# @lc code=start
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        b = nums + nums
        nums.sort()
        for i in range(l):
            a = b[i : i + l]
            if nums == a:
                return True
        return False


# @lc code=end

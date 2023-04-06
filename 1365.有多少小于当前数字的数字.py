#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = sorted(nums)
        ret = []
        for num in nums:
            ret.append(new_nums.index(num))
        return ret


# @lc code=end

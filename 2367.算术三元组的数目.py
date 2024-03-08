#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 算术三元组的数目
#

# @lc code=start
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        return sum(x - diff in s and x + diff in s for x in nums)


# @lc code=end

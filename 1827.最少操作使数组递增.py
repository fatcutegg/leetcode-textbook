#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pre = nums[0] - 1
        res = 0
        for i in nums:
            pre = max(pre + 1, i)
            res += pre - i
        return res


# @lc code=end

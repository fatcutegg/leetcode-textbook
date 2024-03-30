#
# @lc app=leetcode.cn id=2815 lang=python3
#
# [2815] 数组中的最大数对和
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        max_val = [-inf] * 10
        for v in nums:
            max_d = max(map(int, str(v)))
            ans = max(ans, v + max_val[max_d])
            max_val[max_d] = max(max_val[max_d], v)
        return ans


# @lc code=end


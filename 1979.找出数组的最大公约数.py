#
# @lc app=leetcode.cn id=1979 lang=python3
#
# [1979] 找出数组的最大公约数
#

# @lc code=start
import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)
        return math.gcd(mx, mn)


# @lc code=end

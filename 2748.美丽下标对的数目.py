#
# @lc app=leetcode.cn id=2748 lang=python3
#
# [2748] 美丽下标对的数目
#

# @lc code=start
from itertools import combinations
from math import gcd
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        return sum(gcd(int(str(x)[0]), y % 10) == 1 for x, y in combinations(nums, 2))


# @lc code=end

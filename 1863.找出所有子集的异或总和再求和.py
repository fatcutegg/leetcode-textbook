#
# @lc app=leetcode.cn id=1863 lang=python3
#
# [1863] 找出所有子集的异或总和再求和
#

# @lc code=start
from functools import reduce
from itertools import combinations
from operator import xor


class Solution(object):
    def subsetXORSum(self, nums):
        return sum(
            reduce(xor, l)
            for n in range(1, len(nums) + 1)
            for l in combinations(nums, n)
        )


# @lc code=end

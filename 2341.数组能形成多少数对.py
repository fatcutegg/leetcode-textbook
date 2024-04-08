#
# @lc app=leetcode.cn id=2341 lang=python3
#
# [2341] 数组能形成多少数对
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        same_count = diff_count = 0
        c = Counter(nums)
        for v in c.values():
            if v % 2:
                diff_count += 1
            same_count += v // 2
        return [same_count, diff_count]


# @lc code=end

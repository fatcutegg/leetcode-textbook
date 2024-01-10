#
# @lc app=leetcode.cn id=2570 lang=python3
#
# [2570] 合并两个二维数组 - 求和法
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        d = Counter()
        for x, y in nums1:
            d[x] += y
        for x, y in nums2:
            d[x] += y
        return list(sorted(d.items()))


# @lc code=end

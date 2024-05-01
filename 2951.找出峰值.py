#
# @lc app=leetcode.cn id=2951 lang=python3
#
# [2951] 找出峰值
#

# @lc code=start
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        l = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                l.append(i)
        return l


# @lc code=end

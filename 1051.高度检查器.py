#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
from typing import List


class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        c = sorted(heights)
        cnt = 0
        for i, j in zip(heights, c):
            if i != j:
                cnt += 1

        return cnt


# @lc code=end

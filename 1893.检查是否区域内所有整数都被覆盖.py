#
# @lc app=leetcode.cn id=1893 lang=python3
#
# [1893] 检查是否区域内所有整数都被覆盖
#

# @lc code=start
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52  # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True


# @lc code=end

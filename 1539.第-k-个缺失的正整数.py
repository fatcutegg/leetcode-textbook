#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#


# @lc code=start
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missCount = 0
        lastMiss = -1
        current = 1
        ptr = 0

        while missCount < k:
            if current == arr[ptr]:
                if ptr + 1 < len(arr):
                    ptr += 1
            else:
                missCount += 1
                lastMiss = current
            current += 1

        return lastMiss


# @lc code=end

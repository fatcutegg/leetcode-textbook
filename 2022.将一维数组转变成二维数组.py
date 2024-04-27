#
# @lc app=leetcode.cn id=2022 lang=python3
#
# [2022] 将一维数组转变成二维数组
#

# @lc code=start
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        N = len(original)
        if N != m * n:
            return []
        result = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                result[row][col] = original[row * n + col]
        return result


# @lc code=end

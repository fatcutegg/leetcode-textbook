#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
from typing import List
import math


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = n // 4 + 1
        for i in range(n - cnt + 1):
            if arr[i] == arr[i + cnt - 1]:
                return arr[i]


# @lc code=end
arr = [1, 2, 3, 4, 4]
print(Solution().findSpecialInteger(arr))
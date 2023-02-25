#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
from typing import List


class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        while idx < len(arr) - 1:
            if arr[idx] == 0:
                arr[idx + 1:] = [0] + arr[idx + 1:-1]
                idx += 1
            idx += 1


# @lc code=end

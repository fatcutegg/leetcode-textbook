#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n - 2):
            if arr[i] & 1 and arr[i + 1] & 1 and arr[i + 2] & 1:
                return True
        return False

# @lc code=end


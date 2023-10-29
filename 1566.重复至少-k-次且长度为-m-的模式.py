#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#

# @lc code=start
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i = 0
        while i < len(arr):
            p = arr[i:i + m]
            if p * k == arr[i:i + m * k]:
                return True
            i += 1
        return False


# @lc code=end

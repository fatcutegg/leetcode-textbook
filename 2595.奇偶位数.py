#
# @lc app=leetcode.cn id=2595 lang=python3
#
# [2595] 奇偶位数
#


# @lc code=start
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = 0
        while n:
            ans[i] += n & 1
            n >>= 1
            i ^= 1
        return ans


# @lc code=end

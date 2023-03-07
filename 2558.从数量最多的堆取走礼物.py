#
# @lc app=leetcode.cn id=2558 lang=python3
#
# [2558] 从数量最多的堆取走礼物
#

# @lc code=start
from math import sqrt, floor
from typing import List


class Solution:

    def pickGifts(self, gifts: List[int], k: int) -> int:
        step = 0
        while step < k:
            gifts.sort()
            gifts[-1] = floor(sqrt(gifts[-1]))
            step += 1
        return sum(gifts)


# @lc code=end

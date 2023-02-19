#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
from typing import List


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            stones.sort()
            if stones[-2] == stones[-1]:
                stones = stones[:-2]
            else:
                stones = [abs(stones[-2] - stones[-1])] + stones[:-2]
        return stones[0] if stones else 0


# @lc code=end

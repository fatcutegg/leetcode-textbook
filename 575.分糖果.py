#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
import math
from typing import List


class Solution:

    def distributeCandies(self, candyType: List[int]) -> int:

        return int(min(len(candyType) / 2, len(set(candyType))))


# @lc code=end
print(Solution().distributeCandies(candyType=[6,6,6,6]))
#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#


# @lc code=start
from typing import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = Counter(sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1))
        return max(count.values())


# @lc code=end

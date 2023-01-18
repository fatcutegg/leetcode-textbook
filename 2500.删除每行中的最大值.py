#
# @lc app=leetcode.cn id=2500 lang=python3
#
# [2500] 删除每行中的最大值
#

# @lc code=start
from typing import List


class Solution:

    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in zip(*list(map(lambda x: sorted(x, reverse=True), grid))):
            ans += max(i)
        return ans


# @lc code=end

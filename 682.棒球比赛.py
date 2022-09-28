#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        points = []
        for op in operations:
            if op == '+':
                pt = points[-1] + points[-2]
            elif op == 'D':
                pt = points[-1] * 2
            elif op == 'C':
                ans -= points.pop()
                continue
            else:
                pt = int(op)
            ans += pt
            points.append(pt)
        return ans

# @lc code=end


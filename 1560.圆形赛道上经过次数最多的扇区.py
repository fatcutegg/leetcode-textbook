#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        if s <= e:
            # [起点, 终点]
            return list(range(s, e + 1))
        else:
            # [1, 终点]+[起点, n]
            return list(range(1, e + 1)) + list(range(s, n + 1))

# @lc code=end


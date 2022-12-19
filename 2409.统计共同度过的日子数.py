#
# @lc app=leetcode.cn id=2409 lang=python3
#
# [2409] 统计共同度过的日子数
#

# @lc code=start
from datetime import date


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str, D = lambda s: date(2022, *map(int, s.split('-')))) -> int:
        return max(0, (D(min(leaveAlice, leaveBob)) - D(max(arriveAlice, arriveBob))).days + 1)

# @lc code=end


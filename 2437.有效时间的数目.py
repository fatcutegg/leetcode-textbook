#
# @lc app=leetcode.cn id=2437 lang=python3
#
# [2437] 有效时间的数目
#

# @lc code=start
class Solution:
    def countTime(self, time: str) -> int:
        hh = mm = 1
        if time[0] != "?" and time[1] == "?":
            hh *= 10 if time[0] <= "1" else 4
        elif time[0] == "?" and time[1] != "?":
            hh *= 3 if time[1] <= "3" else 2
        elif time[0] == "?" and time[1] == "?":
            hh *= 24

        if time[3] == "?" and time[4] != "?":
            mm *= 6
        elif time[3] != "?" and time[4] == "?":
            mm *= 10
        elif time[3] == "?" and time[4] == "?":
            mm *= 60
        return hh * mm

# @lc code=end


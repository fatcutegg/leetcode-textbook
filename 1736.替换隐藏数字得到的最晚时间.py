#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#


# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == "?":
            time[0] = "2" if time[1] in ("0", "1", "2", "3", "?") else "1"
        if time[1] == "?":
            time[1] = "9" if time[0] in ("0", "1") else "3"
        if time[3] == "?":
            time[3] = "5"
        if time[4] == "?":
            time[4] = "9"
        return "".join(time)


# @lc code=end

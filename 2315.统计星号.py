#
# @lc app=leetcode.cn id=2315 lang=python3
#
# [2315] 统计星号
#


# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        valid = True
        res = 0
        for c in s:
            if c == "|":
                valid = not valid
            elif c == "*" and valid:
                res += 1
        return res


# @lc code=end

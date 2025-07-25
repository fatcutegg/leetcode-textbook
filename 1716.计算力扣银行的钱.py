#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#


# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = 1, 1
        res = 0
        for i in range(n):
            res += week + day - 1
            day += 1
            if day == 8:
                day = 1
                week += 1
        return res


# @lc code=end

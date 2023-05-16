#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#


# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottle, ans = numBottles, numBottles
        while bottle >= numExchange:
            bottle -= numExchange
            ans += 1
            bottle += 1
        return ans


# @lc code=end

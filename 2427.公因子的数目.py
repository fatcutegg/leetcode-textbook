#
# @lc app=leetcode.cn id=2427 lang=python3
#
# [2427] 公因子的数目
#

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans

# @lc code=end


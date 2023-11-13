#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#


# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                ans += n // 2
                n //= 2
            else:
                ans += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return ans


# @lc code=end

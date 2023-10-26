#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        nss = ".".join([str(n)[::-1][i:i+3] for i in range(0, len(str(n)), 3)])
        return nss[::-1]
print(Solution().thousandSeparator(0))
# @lc code=end


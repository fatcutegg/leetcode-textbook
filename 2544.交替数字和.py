#
# @lc app=leetcode.cn id=2544 lang=python3
#
# [2544] 交替数字和
#


# @lc code=start
class Solution:

    def alternateDigitSum(self, n: int) -> int:
        mark = 1
        ans = int(str(n)[0])
        for i in str(n)[1:]:
            mark *= -1
            ans += mark * int(i)
        return ans


# @lc code=end

#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#


# @lc code=start
class Solution:

    def countDigits(self, num: int) -> int:
        ans = 0
        for i in str(num):
            if num % int(i) == 0:
                ans += 1
        return ans


# @lc code=end

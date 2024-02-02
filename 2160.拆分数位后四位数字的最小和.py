#
# @lc app=leetcode.cn id=2160 lang=python3
#
# [2160] 拆分数位后四位数字的最小和
#


# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits.sort()
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]


# @lc code=end

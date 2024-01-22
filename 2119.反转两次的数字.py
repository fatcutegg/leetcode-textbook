#
# @lc app=leetcode.cn id=2119 lang=python3
#
# [2119] 反转两次的数字
#


# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0


# @lc code=end

#
# @lc app=leetcode.cn id=2710 lang=python3
#
# [2710] 移除字符串中的尾随零
#


# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")


# @lc code=end

#
# @lc app=leetcode.cn id=2169 lang=python3
#
# [2169] 得到 0 的操作数
#


# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0  # 相减操作的总次数
        while num1 and num2:
            # 每一步辗转相除操作
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res


# @lc code=end

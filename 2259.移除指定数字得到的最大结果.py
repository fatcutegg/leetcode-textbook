#
# @lc app=leetcode.cn id=2259 lang=python3
#
# [2259] 移除指定数字得到的最大结果
#


# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        res = ""  # 可以得到的最大结果
        for i in range(n):
            if number[i] == digit:
                tmp = number[:i] + number[i + 1 :]
                res = max(res, tmp)
        return res


# @lc code=end

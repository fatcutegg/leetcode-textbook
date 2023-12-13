#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#


# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                # 找到第一个值为奇数的字符，返回 num[0:i+1]
                return num[: i + 1]
        # 未找到值为奇数的字符，返回空字符串
        return ""


# @lc code=end

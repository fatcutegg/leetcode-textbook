#
# @lc app=leetcode.cn id=2264 lang=python3
#
# [2264] 字符串中最大的 3 位相同数字
#


# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = ""
        a = -1
        i = 0
        while i < len(num) - 2:
            if num[i] == num[i + 1] == num[i + 2] and int(num[i]) > a:
                a = int(num[i])
                n = f"{num[i]}{num[i+1]}{num[i+2]}"
            i += 1
        return n


# @lc code=end

#
# @lc app=leetcode.cn id=1844 lang=python3
#
# [1844] 将所有数字用字符替换
#


# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        for i in range(1, n, 2):
            arr[i] = chr(ord(arr[i - 1]) + int(arr[i]))
        return "".join(arr)


# @lc code=end

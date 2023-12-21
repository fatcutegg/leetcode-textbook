#
# @lc app=leetcode.cn id=1945 lang=python3
#
# [1945] 字符串转化后的各位数字之和
#


# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = "".join(str(ord(ch) - ord("a") + 1) for ch in s)

        for i in range(k):
            if len(digits) == 1:
                break
            total = sum(int(ch) for ch in digits)
            digits = str(total)

        return int(digits)


# @lc code=end

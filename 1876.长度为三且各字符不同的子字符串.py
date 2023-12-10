#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#


# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                res += 1
        return res


# @lc code=end

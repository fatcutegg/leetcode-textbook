#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#


# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = "aeiouAEIOU"
        a, b = s[: len(s) // 2], s[len(s) // 2 :]
        return sum(c in VOWELS for c in a) == sum(c in VOWELS for c in b)


# @lc code=end

#
# @lc app=leetcode.cn id=2696 lang=python3
#
# [2696] 删除子串后的字符串最小长度
#


# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "").replace("CD", "")
        return len(s)


# @lc code=end

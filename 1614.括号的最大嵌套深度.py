#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#


# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans, size = 0, 0
        for ch in s:
            if ch == "(":
                size += 1
                ans = max(ans, size)
            elif ch == ")":
                size -= 1
        return ans


# @lc code=end

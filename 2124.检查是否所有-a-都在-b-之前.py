#
# @lc app=leetcode.cn id=2124 lang=python3
#
# [2124] 检查是否所有 A 都在 B 之前
#

# @lc code=start


class Solution:
    def checkString(self, s: str) -> bool:
        return list(s) == sorted(s)


# @lc code=end

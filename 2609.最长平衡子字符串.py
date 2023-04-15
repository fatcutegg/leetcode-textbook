#
# @lc app=leetcode.cn id=2609 lang=python3
#
# [2609] 最长平衡子字符串
#


# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = pre = cur = 0
        for i, x in enumerate(s):
            cur += 1
            if i == len(s) - 1 or x != s[i + 1]:
                if x == "1":
                    ans = max(ans, min(pre, cur) * 2)
                pre = cur
                cur = 0
        return ans


# @lc code=end

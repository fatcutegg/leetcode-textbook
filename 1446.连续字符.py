#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#


# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        ans, cnt = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans


# @lc code=end

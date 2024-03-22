#
# @lc app=leetcode.cn id=2278 lang=python3
#
# [2278] 字母在字符串中的百分比
#


# @lc code=start
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        cnt = 0
        for ch in s:
            if ch == letter:
                cnt += 1
        return 100 * cnt // n


# @lc code=end

#
# @lc app=leetcode.cn id=2566 lang=python3
#
# [2566] 替换一个数字后的最大差值
#


# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:
        mx = num
        s = str(num)
        for c in s:
            if c != "9":
                mx = int(s.replace(c, "9"))
                break
        return mx - int(s.replace(s[0], "0"))


# @lc code=end

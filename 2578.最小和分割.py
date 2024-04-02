#
# @lc app=leetcode.cn id=2578 lang=python3
#
# [2578] 最小和分割
#


# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:
        stnum = "".join(sorted(str(num)))
        num1, num2 = int(stnum[::2]), int(stnum[1::2])
        return num1 + num2


# @lc code=end

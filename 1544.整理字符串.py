#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        ret = []
        for i in s:
            if ret and ret[-1].lower() == i.lower() and ret[-1] != i:
                ret.pop()
            else:
                ret.append(i)
        return "".join(ret)
# @lc code=end



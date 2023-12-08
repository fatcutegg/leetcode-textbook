#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = lambda x:x[-1])
        res = s[0][:-1]
        for i in range(1,len(s)):
            res += ' '+s[i][:-1]
        return res

# @lc code=end


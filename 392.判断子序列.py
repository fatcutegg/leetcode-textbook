#
# @lc app=leetcode.cn id=392 lang=python
#
# [392] 判断子序列
#


# @lc code=start
class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# @lc code=end
s = "aaaaaa"
t = "bbaaaa"
print(Solution().isSubsequence(s, t))

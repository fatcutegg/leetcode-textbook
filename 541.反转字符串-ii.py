#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#


# @lc code=start
class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        t = list(s)
        for i in range(0, len(s), 2 * k):
            t[i:i + k] = reversed(s[i:i + k])
        return "".join(t)


# @lc code=end

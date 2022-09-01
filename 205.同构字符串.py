#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s,t)))
# @lc code=end
s = "foo"
t = "bar"
print(Solution().isIsomorphic(s,t))

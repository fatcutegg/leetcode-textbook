#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#
import math


# @lc code=start
class Solution(object):

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(0, int(math.ceil(len(s) / 2))):
            s[i], s[len(s)-i -1] = s[len(s)-i -1], s[i]
        return s


# @lc code=end

s = ["H","a","n","n","a","h"]
print(Solution().reverseString(s))
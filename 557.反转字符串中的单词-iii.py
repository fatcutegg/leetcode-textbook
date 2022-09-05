#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x: "".join(list(reversed(x))), s.split(" ")))
            
# @lc code=end
s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))


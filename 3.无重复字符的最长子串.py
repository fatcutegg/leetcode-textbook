#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        n = len(s)
        r = 0 # 就要从0开始
        ans = 0
        for i in range(n):
            if i != 0:
                del d[s[i - 1]]
            while r < n and s[r] not in d:
                d[s[r]] = r
                r += 1
            ans = max(ans, r - i)
        return ans


# @lc code=end

s = "bbbbb"

print(Solution().lengthOfLongestSubstring(s))

#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#

# @lc code=start
import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

# @lc code=end


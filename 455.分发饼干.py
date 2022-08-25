#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#


# @lc code=start
class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0
        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            j += 1
            i += 1
        return count


# @lc code=end

g = [1, 2, 3]
s = [1, 1]

print(Solution().findContentChildren(g,s))

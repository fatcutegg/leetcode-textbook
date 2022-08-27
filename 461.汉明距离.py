#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start


class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")


# @lc code=end

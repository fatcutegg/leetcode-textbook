#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start

from math import sqrt


class Solution(object):

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]


# @lc code=end

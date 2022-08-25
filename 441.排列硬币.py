#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#


# @lc code=start
class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left


# @lc code=end

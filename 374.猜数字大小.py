#
# @lc app=leetcode.cn id=374 lang=python
#
# [374] 猜数字大小
#


# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0



class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid
            else:
                left = mid+1
        return left


# @lc code=end

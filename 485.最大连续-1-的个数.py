#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#


# @lc code=start
class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(max("".join(map(str, nums)).split("0"), key=len))


# @lc code=end

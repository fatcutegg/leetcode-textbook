#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 丢失的数字
#


# @lc code=start
class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i, n in enumerate(nums):
            xor ^= i ^ n
        return xor ^ len(nums)


# @lc code=end

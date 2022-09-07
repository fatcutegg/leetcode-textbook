#
# @lc app=leetcode.cn id=561 lang=python
#
# [561] 数组拆分
#


# @lc code=start
class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])


# @lc code=end

print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))

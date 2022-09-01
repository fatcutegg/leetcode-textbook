#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums) >= 3 else nums[0]
# @lc code=end


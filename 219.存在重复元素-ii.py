#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#


# @lc code=start
class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

# @lc code=end
nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums,k))
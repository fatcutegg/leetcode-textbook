#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

# @lc code=end

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(Solution().intersection(nums1,nums2))
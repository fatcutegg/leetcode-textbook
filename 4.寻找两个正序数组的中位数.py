#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        l = len(nums3)
        if l % 2==0:
            mid = int(l/2)
            return (nums3[mid] + nums3[mid-1])/2
        return float(nums3[math.floor(l/2)])


num1 = [1,2]
num2 = [3,4]

print(Solution().findMedianSortedArrays(num1,num2))
# @lc code=end


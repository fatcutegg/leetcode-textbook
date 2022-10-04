#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            ans = nums[mid]
            if ans == target:
                return mid
            if ans > target:
                right = mid - 1
            if ans < target:
                left = mid + 1
        return -1


# @lc code=end

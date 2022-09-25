#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
from typing import List


class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = start = 0
        n = len(nums)
        if n == 1:
            return 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                start = i
            ans = max(ans, i - start + 1)
        return ans


# @lc code=end

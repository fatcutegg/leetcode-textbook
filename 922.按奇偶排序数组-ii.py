#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
from typing import List


class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [_ for _ in range(0, n)]
        i = 0
        for x in nums:
            if x % 2 == 0:
                ans[i] = x
                i += 2
        i = 1
        for x in nums:
            if x % 2 == 1:
                ans[i] = x
                i += 2
        return ans


# @lc code=end

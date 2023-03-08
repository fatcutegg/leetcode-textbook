#
# @lc app=leetcode.cn id=2562 lang=python3
#
# [2562] 找出数组的串联值
#

# @lc code=start
from typing import List


class Solution:

    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            if len(nums) == 1:
                ans += nums[0]
                nums.pop()
            else:
                ans += int(str(nums[0]) + str(nums[-1]))
                nums = nums[1:-1]
        return ans


# @lc code=end

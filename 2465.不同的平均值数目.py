#
# @lc app=leetcode.cn id=2465 lang=python3
#
# [2465] 不同的平均值数目
#

# @lc code=start
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans =[]
        nums = sorted(nums,reverse=True)
        while nums:
            ans.append((nums[0]+nums[-1])/2)
            nums = nums[1:-1]
        return len(set(ans))
# @lc code=end


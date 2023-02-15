#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
from typing import List


class Solution:

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        target = nums[0]
        ans = [target % 5 == 0]
        for i in nums[1:]:
            target = target << 1
            if i:
                target += 1
            ans.append(target % 5 == 0)
        return ans


# @lc code=end

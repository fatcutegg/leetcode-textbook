#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev = -1
        for i in range(n):
            if nums[i] == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        return True


# @lc code=end

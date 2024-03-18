#
# @lc app=leetcode.cn id=2784 lang=python3
#
# [2784] 检查数组是否是好的
#

# @lc code=start
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        cnt = [0] * (n + 1)
        for v in nums:
            if v > n or v == n and cnt[v] > 1 or v < n and cnt[v]:
                return False
            cnt[v] += 1
        return True


# @lc code=end

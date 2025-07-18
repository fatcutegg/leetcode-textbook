#
# @lc app=leetcode.cn id=2176 lang=python3
#
# [2176] 统计数组中相等且可以被整除的数对
#


# @lc code=start
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0  # 符合要求数对个数
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    res += 1
        return res


# @lc code=end

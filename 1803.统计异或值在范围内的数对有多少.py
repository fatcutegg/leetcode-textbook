#
# @lc app=leetcode.cn id=1803 lang=python3
#
# [1803] 统计异或值在范围内的数对有多少
#

# @lc code=start
from typing import List


class Solution:

    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        ans = 0
        n_l = len(nums)
        for i in range(0, n_l):
            for j in range(i + 1, n_l):
                if low <= (nums[i] ^ nums[j]) <= high:
                    ans += 1
                if j + 1 == n_l:
                    if i + 2 == n_l:
                        break
                    continue
        return ans


# @lc code=end

nums = [1, 4, 2, 7]
low = 2
high = 6

print(Solution().countPairs(nums=nums, low=low, high=high))

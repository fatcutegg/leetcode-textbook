#
# @lc app=leetcode.cn id=2248 lang=python3
#
# [2248] 多个数组求交集
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        res = set(nums[0])
        for i in range(1, n):
            tmp = set()
            for num in nums[i]:
                if num in res:
                    tmp.add(num)
            res = tmp
        return sorted(res)


# @lc code=end


#
# @lc app=leetcode.cn id=2869 lang=python3
#
# [2869] 收集元素的最少操作次数
#


# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        vis = [0] * (k + 1)
        cnt = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            # 题目中已经保证输入为正整数
            if nums[i] <= k and not vis[nums[i]]:
                # 对于新加入集合的数进行统计
                vis[nums[i]] = 1
                cnt += 1
                if cnt == k:
                    return n - i


# @lc code=end

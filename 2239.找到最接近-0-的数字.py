#
# @lc app=leetcode.cn id=2239 lang=python3
#
# [2239] 找到最接近 0 的数字
#

# @lc code=start
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]  # 已遍历元素中绝对值最小且数值最大的元素
        dis = abs(nums[0])  # 已遍历元素的最小绝对值
        for num in nums:
            if abs(num) < dis:
                dis = abs(num)
                res = num
            elif abs(num) == dis:
                res = max(res, num)
        return res


# @lc code=end

#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [None for _ in index]
        for idx, i in enumerate(index):
            target = target[:i] + [nums[idx]] + target[i:]
        return target[:len(index)]
# @lc code=end

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(Solution().createTargetArray(nums=nums,index=index))
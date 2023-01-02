#
# @lc app=leetcode.cn id=2455 lang=python3
#
# [2455] 可被三整除的偶数的平均值
#

# @lc code=start
import math
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if i % 3 == 0 and i % 2 ==0:
                ans.append(i)
        if not ans:
            return 0
        return math.floor(sum(ans)/len(ans))
# @lc code=end


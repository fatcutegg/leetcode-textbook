#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#

# @lc code=start
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans += 1 if len(str(i)) % 2 == 0 else 0
        return ans


# @lc code=end

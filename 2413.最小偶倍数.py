#
# @lc app=leetcode.cn id=2413 lang=python3
#
# [2413] 最小偶倍数
#

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return  n  if n % 2 == 0  else n*2

# @lc code=end


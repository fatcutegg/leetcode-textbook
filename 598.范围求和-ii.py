#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
from typing import List
from operator import mul


class Solution:

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return mul(*map(min, zip(*ops))) if ops else m * n


# @lc code=end
m = 3; n = 3; ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
m = 3; n = 3; ops = []
print(Solution().maxCount(m,n,ops))
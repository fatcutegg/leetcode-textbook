#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#

# @lc code=start
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1 - n, n, 2))


# @lc code=end

#
# @lc app=leetcode.cn id=2451 lang=python3
#
# [2451] 差值数组不同的字符串
#

# @lc code=start
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)
        for s in words:
            d[tuple(ord(x) - ord(y) for x, y in pairwise(s))].append(s)
        x, y = d.values()
        return x[0] if len(x) == 1 else y[0]

# @lc code=end


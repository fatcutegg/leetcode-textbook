#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
from collections import Counter
from functools import reduce
from typing import List


class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        # Counter & 运算，取交集
        return list(reduce(lambda x, y: x & y, map(Counter, words)).elements())


# @lc code=end

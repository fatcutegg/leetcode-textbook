#
# @lc app=leetcode.cn id=2496 lang=python3
#
# [2496] 数组中字符串的最大值
#

# @lc code=start
from typing import List


class Solution:

    def maximumValue(self, strs: List[str]) -> int:
        return max(map(lambda x: int(x) if x.isdigit() else len(x), strs))


# @lc code=end

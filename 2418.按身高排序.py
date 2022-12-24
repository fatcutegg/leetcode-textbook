#
# @lc app=leetcode.cn id=2418 lang=python3
#
# [2418] 按身高排序
#

# @lc code=start
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]

# @lc code=end


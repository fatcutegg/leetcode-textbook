#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)


# @lc code=end

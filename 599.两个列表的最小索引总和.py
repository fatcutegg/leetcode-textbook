#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
from typing import List


class Solution:

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cnt = {x: list1.index(x) + list2.index(x) for x in (set(list1) & set(list2))}
        return list(filter(lambda x: cnt[x] == min(cnt.values()), cnt))


# @lc code=end

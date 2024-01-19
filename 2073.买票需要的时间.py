#
# @lc app=leetcode.cn id=2073 lang=python3
#
# [2073] 买票需要的时间
#

# @lc code=start
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        res = 0
        for i in range(n):
            # 遍历计算每个人所需时间
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)
        return res


# @lc code=end

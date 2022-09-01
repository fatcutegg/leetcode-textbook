#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

from typing import List
# @lc code=start


class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans, expired = 0, 0
        for i in range(len(timeSeries)):
            if timeSeries[i] >= expired:
                ans += duration
            else:
                ans += timeSeries[i] + duration - expired
            expired = timeSeries[i] + duration
        return ans


# @lc code=end

#
# @lc app=leetcode.cn id=2511 lang=python3
#
# [2511] 最多可以摧毁的敌人城堡数目
#

# @lc code=start
from typing import List


class Solution:

    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        for i, x in enumerate(forts):
            if x != 1:
                continue
            j = i - 1
            while j >= 0 and forts[j] == 0:
                j -= 1
            if j >= 0 and forts[j] < 0:
                ans = max(ans, i - j - 1)
            j = i + 1
            while j < len(forts) and forts[j] == 0:
                j += 1
            if j < len(forts) and forts[j] < 0:
                ans = max(ans, j - i - 1)
        return ans


# @lc code=end

#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = total = 0
        for x in gain:
            total += x
            ans = max(ans, total)
        return ans


# @lc code=end

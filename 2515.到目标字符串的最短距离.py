#
# @lc app=leetcode.cn id=2515 lang=python3
#
# [2515] 到目标字符串的最短距离
#

# @lc code=start
from typing import List


class Solution:

    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = n = len(words)
        for i, x in enumerate(words):
            if x == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans if ans < n else -1


# @lc code=end

#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 其他人都选他
        inDegrees = Counter(y for _, y in trust)
        # 他没选任何人
        outDegrees = Counter(x for x, _ in trust)
        return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)


# @lc code=end

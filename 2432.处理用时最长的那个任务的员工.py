#
# @lc app=leetcode.cn id=2432 lang=python3
#
# [2432] 处理用时最长的那个任务的员工
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans, max_t = logs[0]
        for (_, t1), (i, t) in pairwise(logs):
            t -= t1
            if t > max_t or t == max_t and i < ans:
                ans, max_t = i, t
        return ans

# @lc code=end


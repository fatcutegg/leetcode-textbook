#
# @lc app=leetcode.cn id=2138 lang=python3
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

# @lc code=start
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []  # 分组后的字符串
        n = len(s)
        curr = 0  # 每个分组的起始下标
        # 拆分字符串
        while curr < n:
            res.append(s[curr : curr + k])
            curr += k
        # 尝试填充最后一组
        res[-1] += fill * (k - len(res[-1]))
        return res


# @lc code=end

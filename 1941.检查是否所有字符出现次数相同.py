#
# @lc app=leetcode.cn id=1941 lang=python3
#
# [1941] 检查是否所有字符出现次数相同
#

# @lc code=start
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)  # 每个字符的实际频数
        occ = len(s) // len(freq)  # 每个字符的理论频数
        return all(v == occ for v in freq.values())


# @lc code=end

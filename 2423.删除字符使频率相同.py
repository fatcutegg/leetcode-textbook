#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#

# @lc code=start
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            cnt = Counter(word[:i] + word[i + 1:])
            same = cnt.popitem()[1]
            if all(c == same for c in cnt.values()):
                return True
        return False

# @lc code=end


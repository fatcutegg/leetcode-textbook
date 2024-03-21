#
# @lc app=leetcode.cn id=1897 lang=python3
#
# [1897] 重新分配字符使所有字符串都相等
#

# @lc code=start
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = [0] * 26  # 每种字符的频数
        n = len(words)
        for wd in words:
            for ch in wd:
                cnt[ord(ch) - ord("a")] += 1
        return all(k % n == 0 for k in cnt)


# @lc code=end

#
# @lc app=leetcode.cn id=1967 lang=python3
#
# [1967] 作为子字符串出现在单词中的字符串数目
#

# @lc code=start
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            for i in range(n - m + 1):
                flag = True
                for j in range(m):
                    if word[i + j] != pattern[j]:
                        flag = False
                        break
                if flag:
                    return True
            return False

        res = 0
        for pattern in patterns:
            res += check(pattern, word)
        return res


# @lc code=end

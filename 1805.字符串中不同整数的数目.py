#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(list(map(int, re.findall("\d+", word)))))


# @lc code=end

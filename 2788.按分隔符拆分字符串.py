#
# @lc app=leetcode.cn id=2788 lang=python3
#
# [2788] 按分隔符拆分字符串
#

# @lc code=start
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res += [sub for sub in word.split(separator) if len(sub)]
        return res


# @lc code=end

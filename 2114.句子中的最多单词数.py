#
# @lc app=leetcode.cn id=2114 lang=python3
#
# [2114] 句子中的最多单词数
#


# @lc code=start
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        for i in sentences:
            ans.append(len(i.split(" ")))
        return max(ans)


# @lc code=end

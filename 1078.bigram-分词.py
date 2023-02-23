#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
from typing import List


class Solution:

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        words = text.split(" ")
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
        return ans


# @lc code=end

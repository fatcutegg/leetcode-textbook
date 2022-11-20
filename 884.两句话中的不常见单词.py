#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = Counter(s1.split()) + Counter(s2.split())
        
        ans = list()
        for word, occ in freq.items():
            if occ == 1:
                ans.append(word)
        
        return ans

# @lc code=end


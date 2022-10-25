#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
from collections import Counter
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter(
            word.lower() 
            for word in re.split(r'[^\w]+',paragraph) 
            if word 
            and word.lower() not in banned
        ).most_common(1)[0][0]
# @lc code=end


#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)

# @lc code=end

licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]


Solution().shortestCompletingWord(licensePlate,words)
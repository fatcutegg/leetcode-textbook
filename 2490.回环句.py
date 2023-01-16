#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#
from itertools import pairwise

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n_s = sentence.split(" ")
        if sentence[-1]!= sentence[0]:
            return False
        for x,y in pairwise(n_s):
            if x[-1] != y[0]:
                return False
        return True
# @lc code=end


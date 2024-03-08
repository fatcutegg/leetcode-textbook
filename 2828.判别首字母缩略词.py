#
# @lc app=leetcode.cn id=2828 lang=python3
#
# [2828] 判别首字母缩略词
#

# @lc code=start
# from typing import List


from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words) == len(s) and all(words[i][0] == s[i] for i in range(len(s)))


# @lc code=end


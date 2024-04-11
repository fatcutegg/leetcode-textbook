#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#


# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        words = [word]
        while "".join(words) in sequence:
            words.append(word)
        return len(words) - 1


# @lc code=end

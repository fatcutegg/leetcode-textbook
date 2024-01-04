#
# @lc app=leetcode.cn id=1880 lang=python3
#
# [1880] 检查某单词是否等于两单词之和
#


# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def decode(word: str) -> int:
            res = 0
            for ch in word:
                res *= 10
                res += ord(ch) - ord("a")
            return res

        return decode(firstWord) + decode(secondWord) == decode(targetWord)


# @lc code=end

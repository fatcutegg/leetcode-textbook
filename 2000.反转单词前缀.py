#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#


# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch) + 1
        return word[:i][::-1] + word[i:]


# @lc code=end

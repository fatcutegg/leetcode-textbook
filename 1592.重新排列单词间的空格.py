#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#


# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * space
        per_space, rest_space = divmod(space, len(words) - 1)
        return (' ' * per_space).join(words) + ' ' * rest_space


# @lc code=end

#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#


# @lc code=start
class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rowIdx = "12210111011122000010020202"
        for word in words:
            idx = rowIdx[ord(word[0].lower()) - ord('a')]
            if all(rowIdx[ord(ch.lower()) - ord('a')] == idx for ch in word):
                ans.append(word)
        return ans


# @lc code=end

#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
        if len(word) >= 2 and word[0].islower() and word[1].isupper():
            return False
        
        # 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
        return all(word[i].islower() == word[1].islower() for i in range(2, len(word)))

# @lc code=end


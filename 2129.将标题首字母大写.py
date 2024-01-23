#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#


# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []  # 辅助数组
        for word in title.split():
            # 对于分割的每个单词按要求处理
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word[0].upper() + word[1:].lower())
        return " ".join(res)


# @lc code=end

#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#


# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mark = "abcdefghijklmnopqrstuvwxyz"
        loaction = []
        key1 = []
        for i in key:
            if i not in key1 and i != " ":
                key1.append(i)
        for i in message:
            if i != " ":
                loaction.append(mark[key1.index(i)])
            else:
                loaction.append(i)
        ans = "".join(loaction)
        return ans


# @lc code=end

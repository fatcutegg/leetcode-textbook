#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lc code=start
class Solution:

    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        for i in s[1:]:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


# @lc code=end

#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#


# @lc code=start
class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        cnt = 0
        start = 0
        for idx, ts in enumerate(s):
            if ts == "(":
                cnt += 1
                if cnt == 1:
                    start = idx
            if ts == ")":
                cnt -= 1
            if cnt == 0:
                ans.append(s[start + 1:idx])
        return "".join(ans)


# @lc code=end
s = "(()())(())"
print(Solution().removeOuterParentheses(s=s))
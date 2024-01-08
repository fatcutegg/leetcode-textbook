#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#


# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        S = [int(i) for i in s.split() if i.isdigit()]
        for i in range(len(S) - 1):
            if S[i] >= S[i + 1]:
                return False
        return True


# @lc code=end

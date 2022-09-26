#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#


# @lc code=start
class Solution:

    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s, i, j):
            for k in range(i, j):
                if s[k] != s[j - k + i]:
                    return False
                if k >= i + (j - i) / 2:
                    break
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s, i + 1, j) or isPalindrome(s, i, j - 1)
            i += 1
            j -= 1
        return True


# @lc code=end
s = "aabdeenddbaagbddeedbaa"
print(Solution().validPalindrome(s=s))

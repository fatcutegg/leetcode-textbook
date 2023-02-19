#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        # 初始化
        dp = [[False] * n for _ in range(n)]  # 二维数组表示起始索引
        for i in range(n):
            dp[i][i] = True  # 单元素也满足回文串

        for L in range(2, n + 1):  # 字串长度
            for left in range(n):
                right = L + left - 1  # 计算出右边界索引
                if right >= n:
                    break
                if s[left] != s[right]:
                    dp[left][right] = False
                else:
                    if right - left < 3:  # 相邻或者仅间隔一个值
                        dp[left][right] = True
                    else:
                        # 判断字串是否满足
                        dp[left][right] = dp[left + 1][right - 1]
                if dp[left][right] and right - left + 1 > max_len:  # 更新最大长度和左边界索引
                    max_len = right - left + 1
                    begin = left
        return s[begin:begin + max_len]


# @lc code=end

print(Solution().longestPalindrome("babad"))
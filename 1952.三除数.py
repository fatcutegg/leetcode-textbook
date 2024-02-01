#
# @lc app=leetcode.cn id=1952 lang=python3
#
# [1952] 三除数
#

# @lc code=start
from math import sqrt


class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i != n // i:
                    # 此时 i 与 n / i 为不同整数
                    cnt += 2
                else:
                    # 此时 i 与 n / i 相等
                    cnt += 1
            i += 1
        return cnt == 3


# @lc code=end

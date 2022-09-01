#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
from itertools import zip_longest


class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        idx = 0
        ans = 0
        for x, y in zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            ans += int(x) * (10**idx)
            ans += int(y) * (10**idx)
            idx += 1
        return str(ans)


# @lc code=end

num1 = "0"
num2 = "0"

print(Solution().addStrings(num1=num1, num2=num2))

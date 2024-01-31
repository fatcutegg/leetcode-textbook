#
# @lc app=leetcode.cn id=2729 lang=python3
#
# [2729] 判断一个数是否迷人
#


# @lc code=start
class Solution:
    def isFascinating(self, n: int) -> bool:
        if n < 123 or n > 329:
            return False
        s = str(n) + str(n * 2) + str(n * 3)
        return "0" not in s and len(set(s)) == 9


# @lc code=end

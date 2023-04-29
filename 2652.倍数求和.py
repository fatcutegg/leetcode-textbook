#
# @lc app=leetcode.cn id=2652 lang=python3
#
# [2652] 倍数求和
#


# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def s(m: int) -> int:
            return (1 + n // m) * (n // m) // 2 * m

        return s(3) + s(5) + s(7) - s(15) - s(21) - s(35) + s(105)


# @lc code=end

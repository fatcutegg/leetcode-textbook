#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num: int) -> bool:
            x = num
            while x:
                x, d = divmod(x, 10)
                if d == 0 or num % d:
                    return False
            return True
        return [i for i in range(left, right + 1) if isSelfDividing(i)]

# @lc code=end


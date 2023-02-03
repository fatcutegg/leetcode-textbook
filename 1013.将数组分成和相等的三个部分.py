#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
from typing import List


class Solution:

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s, t = sum(arr), 0
        if s % 3 != 0:
            return False
        m = 0
        for a in arr:
            t += a
            if t == s // 3:
                m += 1
                t = 0
        return m >= 3


# @lc code=end

#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = k
        for i,j in enumerate(num[::-1]):
            ans += 10**i*j 
        return [int(i) for i in str(ans)]
# @lc code=end


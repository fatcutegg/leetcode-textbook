#
# @lc app=leetcode.cn id=2404 lang=python3
#
# [2404] 出现最频繁的偶数元素
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter()
        for x in nums:
            if x % 2 == 0:
                count[x] += 1
        res, ct = -1, 0
        for k, v in count.items():
            if res == -1 or v > ct or (v == ct and res > k):
                res = k
                ct = v
        return res


# @lc code=end

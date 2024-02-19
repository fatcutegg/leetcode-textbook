#
# @lc app=leetcode.cn id=2206 lang=python3
#
# [2206] 将数组划分成相等数对
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)  # 元素出现次数哈希表
        return all(f % 2 == 0 for f in freq.values())


# @lc code=end

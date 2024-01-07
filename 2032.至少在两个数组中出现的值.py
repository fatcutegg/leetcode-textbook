#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 至少在两个数组中出现的值
#

# @lc code=start
import collections
from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        s = collections.Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        return [i for i in s.keys() if s[i] > 1]


# @lc code=end

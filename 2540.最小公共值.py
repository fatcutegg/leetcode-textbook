#
# @lc app=leetcode.cn id=2540 lang=python3
#
# [2540] 最小公共值
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        counter = Counter(list(set(nums1)) + list(set(nums2)))
        most_common = sorted(list(filter(lambda x: x[1] > 1, counter.most_common())), key=lambda x: x[0], reverse=False)
        return most_common[0][0] if most_common and most_common[0][1] > 1 else -1


# @lc code=end
nums1 = [12, 16, 24, 24, 25, 27, 31, 37, 38, 41, 43, 50, 57, 70, 71, 71, 74, 76, 77, 78]
nums2 = [5, 5, 9, 11, 12, 17, 20, 34, 36, 51, 61, 68, 70, 79, 85, 87, 88, 90, 91, 97]
print(Solution().getCommon(nums1=nums1, nums2=nums2))

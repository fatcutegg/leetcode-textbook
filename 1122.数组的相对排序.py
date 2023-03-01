#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        counter = Counter(arr1)
        for i in arr2:
            if i in counter:
                ans += [i] * counter[i]
                counter.pop(i)
        missNums = []
        for i in counter.keys():
            missNums.extend([i] * counter[i])
        missNums.sort()
        ans.extend(missNums)
        return ans


# @lc code=end
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(Solution().relativeSortArray(arr1, arr2))

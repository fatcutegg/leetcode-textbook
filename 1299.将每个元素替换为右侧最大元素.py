#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans


# @lc code=end

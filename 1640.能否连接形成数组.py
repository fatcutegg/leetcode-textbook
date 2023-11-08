#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] not in index:
                return False
            p = pieces[index[arr[i]]]
            if arr[i : i + len(p)] != p:
                return False
            i += len(p)
        return True


# @lc code=end

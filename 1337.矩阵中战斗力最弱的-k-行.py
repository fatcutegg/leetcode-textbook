#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # return [i[1] for i in sorted([(sum(i), idx) for idx,i in enumerate(mat)], key= lambda x: x[0])][:k]
        return [i[0] for i in sorted(enumerate(map(lambda x: sum(x[1]), enumerate(mat))), key=lambda x: x[1])][:k]
        return sorted([i for i in range(len(mat))],
                      key=lambda x: sum(mat[x]))[:k]


# @lc code=end

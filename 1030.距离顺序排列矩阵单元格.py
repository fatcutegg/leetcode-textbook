#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
from typing import List


class Solution:

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = []
        for i in range(rows):
            for j in range(cols):
                ans.append([abs(i - rCenter) + abs(j - cCenter), i, j])
        ans = sorted(ans, key=lambda x: x[0])
        ans = [[x[1], x[2]] for x in ans]
        return ans


# @lc code=end
rows = 2
cols = 3
rCenter = 1
cCenter = 2
print(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter))

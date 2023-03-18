#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
from itertools import combinations
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 3阶数独矩阵
        SUDOKU = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
        # 如果其中3数和为15就赢
        if 15 in [sum(k) for k in combinations([SUDOKU[i][j] for i, j in moves[::2]], 3)]:
            return "A"
        if 15 in [sum(k) for k in combinations([SUDOKU[i][j] for i, j in moves[1::2]], 3)]:
            return "B"
        return "Draw" if len(moves) == 9 else "Pending"


# @lc code=end
moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
print(Solution().tictactoe(moves))
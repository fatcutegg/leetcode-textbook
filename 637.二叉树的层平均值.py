#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        counts = []
        totals = []

        def dfs(root: TreeNode, level: int):
            if root is None:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]


# @lc code=end

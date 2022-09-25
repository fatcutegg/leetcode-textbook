#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
class Solution:

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans, rootval = -1, root.val

        def dfs(node: TreeNode) -> None:
            nonlocal ans
            if not node:
                return
            if ans != -1 and node.val >= ans:
                return
            if node.val > rootval:
                ans = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans


# @lc code=end

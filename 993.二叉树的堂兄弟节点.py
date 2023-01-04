#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_p, x_d, x_f = None, None, False
        y_p, y_d, y_f = None, None, False

        def dfs(node, depth, parent):
            if not node:
                return
            nonlocal x_p, y_p, x_d, y_d, x_f, y_f
            if node.val == x:
                x_p, x_d, x_f = parent, depth, True
            elif node.val == y:
                y_p, y_d, y_f = parent, depth, True

            dfs(node.left, depth + 1, node)

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_d == y_d and x_p != y_p


# @lc code=end

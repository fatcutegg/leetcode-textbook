#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self.dfs(root, subRoot)

    def dfs(self, root, subRoot):
        if root is None:
            return False
        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot) or self.isSameTree(root, subRoot)

    def isSameTree(self, root, subTree):
        if root is None and subTree is None:
            return True
        if root is None or subTree is None or root.val != subTree.val:
            return False
        return self.isSameTree(root.left, subTree.left) and self.isSameTree(root.right, subTree.right)


# @lc code=end

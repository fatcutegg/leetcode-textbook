#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            left = self.invertTree(root=root.left)
            right = self.invertTree(root=root.right)
            root.left, root.right = right, left
        return root


# @lc code=end

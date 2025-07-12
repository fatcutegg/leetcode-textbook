#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def traversal(root):
            if not root:
                return
            traversal(root=root.left)
            ret.append(root.val)
            traversal(root=root.right)

        traversal(root=root)
        return ret


# @lc code=end

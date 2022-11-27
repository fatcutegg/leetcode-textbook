#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.


class Solution:



    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res = []
        self.inorder(root)

        dummyNode = TreeNode(-1)
        currentNode = dummyNode
        for val in self.res:
            currentNode.right = TreeNode(val)
            currentNode = currentNode.right
        return dummyNode.right

    def inorder(self, node):
        if not node:
            return None
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)


# @lc code=end

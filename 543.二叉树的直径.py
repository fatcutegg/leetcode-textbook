#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if root is None:
                return 0
            r = dfs(root.right)
            l = dfs(root.left)
            self.ans = max(r + l, self.ans)
            return max(r, l) + 1

        dfs(root)
        return self.ans


# @lc code=end

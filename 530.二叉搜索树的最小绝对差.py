#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float("inf")
        self.pre = -1
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        if self.pre == -1:
            self.pre = root.val
        else:
            self.ans = min(self.ans, root.val - self.pre)
            self.pre = root.val
        self.dfs(root.right)


# @lc code=end

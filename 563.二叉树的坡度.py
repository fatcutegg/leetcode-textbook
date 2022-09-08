#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
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

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0
            l_ret = dfs(root.left)
            r_ret = dfs(root.right)
            self.ans += abs(l_ret - r_ret)
            return l_ret + r_ret + root.val

        dfs(root)
        return self.ans


# @lc code=end

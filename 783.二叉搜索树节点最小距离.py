#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        pre = float("-inf")
        res = float("inf")
        def dfs(root):
            nonlocal pre,res
            if not root:
                return
            dfs(root.left)
            res = min(res,root.val-pre)
            pre = root.val
            dfs(root.right)
        dfs(root)
        return res


# @lc code=end


#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(root: TreeNode) -> TreeNode:

            if root == None:
                return None

            if root.val == target.val:
                return root
            
            # left
            result = dfs(root.left)

            # right
            tmp_result = dfs(root.right)

            result =  tmp_result or result

            return result
        
        # solve
        return dfs(cloned)

# @lc code=end


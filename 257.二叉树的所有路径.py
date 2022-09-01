#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def buildPath(root,path):
            if  root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    buildPath(root.left,path)
                    buildPath(root.right, path)
        buildPath(root,"")
        return paths
        
# @lc code=end


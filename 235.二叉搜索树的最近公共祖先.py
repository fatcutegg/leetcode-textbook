#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def getNode(root ,target):
            paths = []
            node = root
            while node != target:
                paths.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            paths.append(node)
            return paths

        p_path = getNode(root,p)
        q_path = getNode(root,q)

        ret = None
        for k,v in zip(p_path,q_path):
            if k == v:
                ret = k
            else:
                break
        return ret




        
# @lc code=end


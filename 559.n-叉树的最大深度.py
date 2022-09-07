#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return max((self.maxDepth(child) for child in root.children), default=0) + 1 if root else 0


# @lc code=end

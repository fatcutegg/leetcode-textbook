#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        result = []
        max_count = count = 0
        base = float("-inf")

        #对当前值进行处理
        def update(x):
            nonlocal max_count, count, base, result
            #相等则计数+1
            if x == base:
                count += 1
            else:
                #不相等，说明该数的节点已经全部遍历完成，更新base，count为1
                base = x
                count = 1
            #计数如果等于max，则加入result
            if count == max_count:
                result.append(base)
            #计数如果大于max，则要重置result，并把该值加入
            if count > max_count:
                max_count = count
                result = []
                result.append(base)

        #二叉查找树，中序遍历，数据从小到大顺序处理
        def mid_order(root):
            if root:
                nonlocal max_count, count, base, result
                mid_order(root.left)
                update(root.val)
                mid_order(root.right)

        mid_order(root)
        return result


# @lc code=end
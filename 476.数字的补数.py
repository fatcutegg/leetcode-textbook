#
# @lc app=leetcode.cn id=476 lang=python
#
# [476] 数字的补数
#


# @lc code=start
class Solution(object):

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        highest = 0
        for i in range(1, 30 + 1):
            if num >= (1 << i):
                highest = i
            else:
                break
        mask = (1 << (highest + 1)) - 1
        return num ^ mask


# @lc code=end
print(Solution().findComplement(2))

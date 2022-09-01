#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#


# @lc code=start
class Solution(object):

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def bka(x):
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones +=1
            return ones
        
        return [bka(i) for i in range(0,n+1)]


# @lc code=end

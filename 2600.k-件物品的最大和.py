#
# @lc app=leetcode.cn id=2600 lang=python3
#
# [2600] K 件物品的最大和
#


# @lc code=start
class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if k >= numOnes:
            k -= numOnes
        else:
            return k
        if k >= numZeros:
            k -= numZeros
        else:
            return numOnes
        return numOnes - k


# @lc code=end

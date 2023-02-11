#
# @lc app=leetcode.cn id=2535 lang=python3
#
# [2535] 数组元素和与数字和的绝对差
#

# @lc code=start
from functools import reduce
from typing import List


class Solution:

    def differenceOfSum(self, nums: List[int]) -> int:
        sum_ele = sum(nums)
        sum_dig = reduce(lambda x, y: int(x) + int(y), "".join([str(i) for i in nums]))

        return abs(sum_ele - sum_dig)


# @lc code=end

#
# @lc app=leetcode.cn id=2553 lang=python3
#
# [2553] 分割数组中数字的数位
#

# @lc code=start
from typing import List


class Solution:

    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.extend([int(_) for _ in str(i)])
        return ans


# @lc code=end
print(Solution().separateDigits([13,25,83,77]))
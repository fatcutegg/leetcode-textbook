#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
from typing import List


class Solution:

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for i in range(num_people)]
        cur_idx = 0
        cur_can = 0
        while candies > 0:
            cur_can += 1
            ans[cur_idx] += min(cur_can, candies)
            candies -= cur_can
            cur_idx = 0 if cur_idx + 1 == num_people else cur_idx + 1
        return ans


# @lc code=end
print(Solution().distributeCandies(7,4))
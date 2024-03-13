#
# @lc app=leetcode.cn id=2678 lang=python3
#
# [2678] 老人的数目
#

# @lc code=start
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for info in details if int(info[11:13]) > 60)


# @lc code=end

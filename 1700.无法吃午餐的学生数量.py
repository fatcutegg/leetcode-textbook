#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

# @lc code=start
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1 = sum(students)
        s0 = len(students) - s1
        for x in sandwiches:
            if x == 0 and s0:
                s0 -= 1
            elif x == 1 and s1:
                s1 -= 1
            else:
                break
        return s0 + s1


# @lc code=end

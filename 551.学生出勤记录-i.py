#
# @lc app=leetcode.cn id=551 lang=python
#
# [551] 学生出勤记录 I
#


# @lc code=start
class Solution(object):

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absents = lates = 0
        for c in s:
            if c == "A":
                absents += 1
                if absents >= 2:
                    return False
            if c == "L":
                lates += 1
                if lates >= 3:
                    return False
            else:
                lates = 0

        return True


# @lc code=end

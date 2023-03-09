#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Annotaion:

    def __init__(self):
        # start\sign\num\other
        self.state_table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

        self.state = "start"
        self.ans = 0
        self.sign = 1

    #进行状态转移
    def get(self, c):
        if c == " ":
            self.state = self.state_table[self.state][0]
        elif c == '+' or c == '-':
            self.state = self.state_table[self.state][1]
            if self.state == "signed" and c == "-":
                self.sign = -1
        elif '9' >= c >= '0':
            self.state = self.state_table[self.state][2]
            if self.state == "in_number":
                self.ans = self.ans * 10 + int(c)
        else:
            self.state = self.state_table[self.state][3]


class Solution:

    def __init__(self):
        self.max_int = 0x7fffffff
        self.min_int = -self.max_int - 1

    def myAtoi(self, s: str) -> int:
        annotaion = Annotaion()
        for c in s:
            annotaion.get(c)
        ans = annotaion.ans * annotaion.sign
        ans = max(self.min_int, min(ans, self.max_int))
        return ans


# @lc code=end
print(Solution().myAtoi("42"))
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        span = numRows * 2 - 2
        left = 0
        right = left + span
        cnt = len(s)
        m1 = []
        while left <= cnt:
            t = s[left:right - (numRows - 2)]
            lt = len(t)
            if lt == 0 :
                break
            m1.append(t.ljust(numRows," "))
            if lt < numRows:
                break
            p = " " + s[left+numRows:right] + " "
            p = p.ljust(numRows," ")
            if p.strip():
                m1.append(p[::-1])
            left = right
            right = left+span
        # print(m1)
        ns = zip(*m1)
        ret = ""
        for i in ns:
            ret+= "".join(i)
        return ret.replace(" ","")


s = "ABCDE"
numRows = 4

print(Solution().convert(s=s,numRows=numRows))

# s = "PAYPALISHIRING"
# numRows = 4
# print(Solution().convert(s=s,numRows=numRows))
# s = "A"
# numRows = 1
# print(Solution().convert(s=s,numRows=numRows))
# s = "PAYPALL"
# numRows = 2
# print(Solution().convert(s=s,numRows=numRows))
# @lc code=end

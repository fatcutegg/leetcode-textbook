#
# @lc app=leetcode.cn id=1869 lang=python3
#
# [1869] 哪种连续子字符串更长
#


# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mx0, mx1 = 0, 0
        cnt = 0
        prev = "#"  # 上个字符
        for ch in s:
            # 当前字符与上个字符相等
            if prev == ch:
                cnt += 1
            # 当前字符与上个字符不相等
            else:
                if prev == "0":
                    mx0 = max(mx0, cnt)
                elif prev == "1":
                    mx1 = max(mx1, cnt)
                cnt = 1
            prev = ch
        # 字符串结尾的连续子串
        if prev == "0":
            mx0 = max(mx0, cnt)
        elif prev == "1":
            mx1 = max(mx1, cnt)
        return mx1 > mx0


# @lc code=end

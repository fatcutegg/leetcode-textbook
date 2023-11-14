#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
import re


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = re.compile(r"[- ]").sub("", number)
        idx, n, ans = 0, len(number), []
        while idx + 4 < n:
            ans.append(number[idx : idx + 3])
            idx += 3
        if n - idx == 4:
            ans.append(number[idx : idx + 2])
            idx += 2
        ans.append(number[idx:n])
        return "-".join(ans)


# @lc code=end

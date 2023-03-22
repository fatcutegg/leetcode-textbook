#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = num
        s_n = str(num)
        for idx, i in enumerate(s_n):
            if i == '6':
                ans = max(ans, int(s_n[:idx]+'9'+s_n[idx+1:]))
        return ans
# @lc code=end


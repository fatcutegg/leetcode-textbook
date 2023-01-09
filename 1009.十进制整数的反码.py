#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        highbit = 0
        for i in range(1, 30 + 1):
            if n >= (1 << i):
                # 找到最高位1
                highbit = i
            else:
                break
        
        mask = (1 << (highbit + 1)) - 1
        # 异或
        return n ^ mask

# @lc code=end


#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2269] 找到一个数字的 K 美丽值
#


# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)  # num 十进制表示字符串
        n = len(s)
        res = 0
        for i in range(n - k + 1):
            # 枚举所有长度为 k 的子串
            tmp = int(s[i : i + k])
            if tmp != 0 and num % tmp == 0:
                res += 1
        return res


# @lc code=end

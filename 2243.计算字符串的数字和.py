#
# @lc app=leetcode.cn id=2243 lang=python3
#
# [2243] 计算字符串的数字和
#


# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []  # 每次操作结束的字符串对应数组
            n = len(s)
            for i in range(0, n, k):
                val = 0
                for j in range(i, min(i + k, n)):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s


# @lc code=end

#
# @lc app=leetcode.cn id=482 lang=python
#
# [482] 密钥格式化
#


# @lc code=start
class Solution(object):

    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans, cnt = [], 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                ans.append(s[i].upper())
                cnt += 1
                if cnt % k == 0:
                    ans.append("-")
        if ans and ans[-1] == "-":
            ans.pop()
        return "".join(ans[::-1])


# @lc code=end
print(Solution().licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))

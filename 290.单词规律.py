#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#


# @lc code=start
class Solution(object):

    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapping = {}
        ss = s.split(" ")
        if len(pattern) != len(ss):
            return False
        for i, j in zip(pattern, ss):
            if i not in mapping:
                if j in mapping.values():
                    return False
                else:
                    mapping[i] = j
            if mapping[i] != j:
                return False
        return True


# @lc code=end

pattern = "abba"
s = "dog cat cat dog"

print(Solution().wordPattern(pattern=pattern, s=s))

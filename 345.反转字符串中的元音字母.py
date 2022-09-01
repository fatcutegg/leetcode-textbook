#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#


# @lc code=start
class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isVowel(v):
            return v in 'aeiouAEIOU'

        left = 0
        n = len(s)

        right = n - 1
        ss = list(s)
        while left < right:
            while left < n and not isVowel(ss[left]):
                left += 1
            while 0 < right and not isVowel(ss[right]):
                right -= 1
            if left < right:
                ss[left], ss[right] = ss[right], ss[left]
                left += 1
                right -= 1
        return "".join(ss)


# @lc code=end

s = "leetcode"
print(Solution().reverseVowels(s))

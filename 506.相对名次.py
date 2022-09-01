#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#

# @lc code=start
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        desc = ("Gold Medal", "Silver Medal", "Bronze Medal")
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        # arr = sorted(enumerate(score), key=lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = desc[i] if i < 3 else str(i + 1)
        return ans

# @lc code=end

print(Solution().findRelativeRanks([10,3,8,9,4]))

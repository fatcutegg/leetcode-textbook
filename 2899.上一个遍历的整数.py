#
# @lc app=leetcode.cn id=2899 lang=python3
#
# [2899] 上一个遍历的整数
#

# @lc code=start
from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = []
        nums = []
        k = 0
        for s in words:
            if s != -1:  # 不是 prev
                nums.append(int(s))
                k = 0
            else:
                k += 1
                ans.append(-1 if k > len(nums) else nums[-k])  # 倒数第 k 个
        return ans



# @lc code=end

print(Solution().lastVisitedIntegers([1,2,-1,-1,-1]))
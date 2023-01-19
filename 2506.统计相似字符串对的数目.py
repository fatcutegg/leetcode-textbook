#
# @lc app=leetcode.cn id=2506 lang=python3
#
# [2506] 统计相似字符串对的数目
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:

    def similarPairs(self, words: List[str]) -> int:
        ans, cnt = 0, Counter()
        for s in words:
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord('a'))
            ans += cnt[mask]
            cnt[mask] += 1
        return ans


# @lc code=end

Solution().similarPairs(["aba","aabb","abcd","bac","aabc"])
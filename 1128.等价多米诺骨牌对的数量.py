#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
from typing import List


class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        mapping = {}
        for i in dominoes:
            i.sort()
            i = [str(_) for _ in i]
            if "".join(i) in mapping or "".join(i)[::-1] in mapping:
                mapping["".join(i)] += 1
            else:
                mapping["".join(i)] = 1
        for i in mapping.values():
            if i == 2:
                ans += 1
            if i > 2:
                ans += i * (i - 1) / 2
        return int(ans)


# @lc code=end
print(Solution().numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))

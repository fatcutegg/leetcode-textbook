#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                # 这个语句在循环体正常结束（没有被break）时执行
                res += 1
            
        return res
# @lc code=end


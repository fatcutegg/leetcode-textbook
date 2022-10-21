#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        MAX_WIDTH = 100
        lines, width = 1, 0
        for c in s:
            need = widths[ord(c) - ord('a')]
            width += need
            if width > MAX_WIDTH:
                lines += 1
                width = need
        return [lines, width]

# @lc code=end


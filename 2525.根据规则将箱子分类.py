#
# @lc app=leetcode.cn id=2525 lang=python3
#
# [2525] 根据规则将箱子分类
#


# @lc code=start
class Solution:

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isHeavy = False
        isBulky = False
        if length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 1000000000:
            isBulky = True
        if mass >= 100:
            isHeavy = True
        if isBulky and isHeavy:
            return "Both"
        elif isBulky and not isHeavy:
            return "Bulky"
        elif not isBulky and isHeavy:
            return "Heavy"
        elif not isBulky and not isHeavy:
            return "Neither"


# @lc code=end

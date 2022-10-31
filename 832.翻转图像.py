#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if image[i][left] == image[i][right]:
                    image[i][left] ^= 1
                    image[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                image[i][left] ^= 1
        return image

# @lc code=end


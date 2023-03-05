#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
import collections
from typing import List


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans


# @lc code=end
words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
print(Solution().countCharacters(words=words, chars=chars))

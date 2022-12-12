#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            i = email.index('@')
            local = email[:i].split('+', 1)[0]  # 去掉本地名第一个加号之后的部分
            local = local.replace('.', '')  # 去掉本地名中所有的句点
            emailSet.add(local + email[i:])
        return len(emailSet)

# @lc code=end


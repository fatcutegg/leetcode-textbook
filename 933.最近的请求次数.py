#
# @lc app=leetcode.cn id=933 lang=python
#
# [933] 最近的请求次数
#

# @lc code=start


class RecentCounter(object):

    def __init__(self):
        self.q = []


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.remove(self.q[0])
        return len(self.q)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end


#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = []


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not key in self.val: self.val.append(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.val: self.val.remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.val


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end


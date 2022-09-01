#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start


class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        low = nums[0]
        tmp = [low]
        for i in nums[1:]:
            if i == low + 1:
                tmp.append(i)
                low = i
            else:
                result.append(tmp)
                low = i
                tmp = [low]
        result.append(tmp)
        ret = []
        for i in result:
            if len(i) > 1:
                ret.append(f"{i[0]}->{i[-1]}")
            else:
                ret.append(f"{i[0]}")
        return ret


# @lc code=end
nums = [0, 2, 3, 4, 6, 8, 9]
print(Solution().summaryRanges(nums))

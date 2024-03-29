--
-- @lc app=leetcode.cn id=619 lang=mysql
--
-- [619] 只出现一次的最大数字
--

-- @lc code=start
# Write your MySQL query statement below
select
    max(num) as num
from 
    (
        select 
            num
        from 
            MyNumbers
        group by num
        having count(num) = 1
    ) t
-- @lc code=end


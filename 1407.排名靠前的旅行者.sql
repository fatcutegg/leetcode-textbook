--
-- @lc app=leetcode.cn id=1407 lang=mysql
--
-- [1407] 排名靠前的旅行者
--

-- @lc code=start
# Write your MySQL query statement below
select 
    name, coalesce(sum(distance), 0) travelled_distance
from 
    users u
left join rides r on u.id=r.user_id
group by u.id
order by travelled_distance desc, name;

-- @lc code=end


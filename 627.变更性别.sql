--
-- @lc app=leetcode.cn id=627 lang=mysql
--
-- [627] 变更性别
--

-- @lc code=start
# Write your MySQL query statement below
update Salary set sex = case sex WHEN 'm' THEN 'f' ELSE 'm' END;
-- @lc code=end


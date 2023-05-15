--
-- @lc app=leetcode.cn id=1517 lang=mysql
--
-- [1517] 查找拥有有效邮箱的用户
--

-- @lc code=start
# Write your MySQL query statement below
# Write your MySQL query statement below

select * from users
where mail REGEXP '^[a-zA-Z][a-zA-Z0-9\_\.\-]*@leetcode\\.com$'

-- @lc code=end


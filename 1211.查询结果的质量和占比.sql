--
-- @lc app=leetcode.cn id=1211 lang=mysql
--
-- [1211] 查询结果的质量和占比
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
    query_name, 
    ROUND(AVG(rating/position), 2) quality,
    ROUND(SUM(IF(rating < 3, 1, 0)) * 100 / COUNT(*), 2) poor_query_percentage
FROM Queries
GROUP BY query_name

-- @lc code=end


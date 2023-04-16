--
-- @lc app=leetcode.cn id=610 lang=mysql
--
-- [610] 判断三角形
--

-- @lc code=start
# Write your MySQL query statement below

SELECT  *
       ,CASE WHEN x+y > z AND x+z > y AND z+y > x THEN "Yes"  ELSE "No" END AS 'triangle'
FROM Triangle

-- @lc code=end


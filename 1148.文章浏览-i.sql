--
-- @lc app=leetcode.cn id=1148 lang=mysql
--
-- [1148] 文章浏览 I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM  Views
WHERE author_id = viewer_id
ORDER BY author_id

-- @lc code=end


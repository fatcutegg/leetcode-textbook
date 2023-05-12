--
-- @lc app=leetcode.cn id=1484 lang=mysql
--
-- [1484] 按日期分组销售产品
--

-- @lc code=start
# WRITE YOUR MYSQL QUERY STATEMENT BELOW

SELECT sell_date,
       COUNT(DISTINCT product) num_sold,
       GROUP_CONCAT(DISTINCT product ORDER BY product ASC) products
FROM Activities
GROUP BY sell_date

-- @lc code=end
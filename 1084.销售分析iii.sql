--
-- @lc app=leetcode.cn id=1084 lang=mysql
--
-- [1084] 销售分析III
--

-- @lc code=start
# Write your MySQL query statement below
select product.product_id,product.product_name from product inner join sales on product.product_id = sales.product_id GROUP BY sales.product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'

-- @lc code=end


--
-- @lc app=leetcode.cn id=1068 lang=mysql
--
-- [1068] 产品销售分析 I
--

-- @lc code=start
# Write your MySQL query statement below
select product_name, year, price from Sales left join Product on Sales.product_id = Product.product_id
-- @lc code=end


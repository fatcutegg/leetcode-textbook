--
-- @lc app=leetcode.cn id=1327 lang=mysql
--
-- [1327] 列出指定时间段内所有的下单产品
--

-- @lc code=start
# Write your MySQL query statement below
select p.product_name,sum(o.unit) as unit
from
    products p
left join
    orders o 
on
    p.product_id=o.product_id
where
    order_date between '2020-02-01' and '2020-02-29'
group by
    p.product_name
having
    sum(o.unit)>=100
order by
    sum(o.unit)

-- @lc code=end


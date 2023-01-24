# Write your MySQL query statement below
select a.id from Weather as a cross join Weather as b on datediff(a.recordDate, b.recordDate) = 1 where a.Temperature > b.Temperature;
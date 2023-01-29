# Write your MySQL query statement below
select class from Courses group by class HAVING COUNT(DISTINCT student) >= 5;
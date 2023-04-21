--
-- @lc app=leetcode.cn id=1378 lang=mysql
--
-- [1378] 使用唯一标识码替换员工ID
--

-- @lc code=start
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT IFNULL(e2.unique_id, NULL) AS 'unique_id',
    e1.name AS 'name'
FROM Employees AS e1
    LEFT  JOIN EmployeeUNI AS e2
    ON e1.id = e2.id
;
-- @lc code=end


--
-- @lc app=leetcode.cn id=1280 lang=mysql
--
-- [1280] 学生们参加各科测试的次数
--

-- @lc code=start
# Write your MySQL query statement below
select
ss.student_id as student_id,
ss.student_name as student_name,
ss.subject_name as subject_name,
ifnull(e1.attended_exams, 0) as attended_exams
from
(
    select
    *
    from `Students` as s1 
    cross join `Subjects` as s2
) as ss
left join
(
    select
    student_id, 
    subject_name,
    count(student_id) as attended_exams
    from `Examinations`
    group by student_id,subject_name
) as e1
on ss.student_id = e1.student_id
and ss.subject_name = e1.subject_name
order by ss.student_id, ss.subject_name

-- @lc code=end


# Write your MySQL query statement below
select name as Employee from Employee e where e.salary > (select salary from Employee a where a.id = e.managerId);
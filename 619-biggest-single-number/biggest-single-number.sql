# Write your MySQL query statement below
select max(a.num) as num from (select * from mynumbers group by num having count(*) = 1) a;
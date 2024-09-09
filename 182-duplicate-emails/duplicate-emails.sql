# Write your MySQL query statement below
select distinct email from Person p where (select count(*) from Person a where a.email = p.email)>1;
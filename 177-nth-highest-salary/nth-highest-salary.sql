CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare temp int;
declare result int;

set temp = (select count(*) from (select distinct salary from employee) a);
if temp<N or N<=0 then
set result = null;
else
set result = (select s.salary from (select distinct salary from employee order by salary desc limit N) s order by s.salary asc limit 1);
end if;
  RETURN result;
END
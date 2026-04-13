# Write your MySQL query statement below
select d.name as Department, e.name as Employee ,Salary
from Employee e join Department d on e.departmentId =d.id
where 3>=(select count(distinct e2.salary) from Employee e2
WHERE e2.DepartmentId = e.DepartmentId AND e2.Salary >= e.Salary)
ORDER BY
    Department, Salary DESC;;

# Write your MySQL query statement below
SELECT (SELECT distinct salary AS SecondHighestSalary from Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary
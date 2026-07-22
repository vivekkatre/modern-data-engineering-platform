/* Use the following schema for all queries:
-- employees
emp_id
emp_name
department
salary
hire_date
city
*/

/* Query 1

Display all employee records. */

SELECT * FROM employees;

/* Query 2

Display only:

emp_name
department
salary */

SELECT emp_name, department, salary FROM employees;

/* Query 3

Display employees whose salary is greater than 60000. */

SELECT emp_name, salary FROM employees
WHERE salary > 60000;

/* Query 4

Display employees who belong to the 'IT' department. */

SELECT emp_name, department FROM employees
WHERE department = 'IT';

/* Query 5

Display employees who are not from 'Delhi' */

SELECT emp_name FROM employees
WHERE city <> "Delhi";

/* Query 6

Display employees ordered by salary in descending order. */

SELECT emp_name, salary FROM employees
ORDER BY salary DESC;

/* Query 7

Display the top 5 highest-paid employees. */

SELECT emp_name FROM employees
ORDER BY salary DESC
LIMIT 5;

/* Query 8

Display unique department names. */

SELECT DISTINCT(department) FROM employees;

/* Query 9

Display employees hired after 2022-01-01. */

SELECT emp_name, hire_date FROM employees
WHERE hire_date > '2022-01-01';

/* Query 10

Display employees whose names start with the letter A. */

SELECT emp_name FROM employees
WHERE emp_name like 'A%';

/* Count total employees.
Find the highest salary.
Find the lowest salary.
Find the average salary.
Count employees in each department. */

SELECT COUNT(*) as total_employees FROM employees;

SELECT MAX(salary) as Max_Salary FROM employees;

SELECT MIN(salary) as Min_Salary FROM employees;

SELECT AVG(salary) as Avg_Salary FROM employees;

SELECT department, count(*) as emp_count_per_department
FROM employees
GROUP BY department;

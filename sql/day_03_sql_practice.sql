/* -- employees
emp_id
emp_name
department
salary
hire_date
city
*/

-- Day 3 Exercises

-- Query 1 – COUNT
SELECT COUNT(*) AS total_employees
FROM employees;

-- Query 2 – DISTINCT
SELECT DISTINCT city
FROM employees;

-- Query 3 – GROUP BY
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;

-- Query 4 – AVG
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;

-- Query 5 – MIN & MAX
SELECT department, MIN(salary) AS minimum_salary, MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;

-- Query 6 – SUM
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;

-- Query 7 – Multiple Aggregates
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS average_salary, MIN(salary) AS minimum_salary, MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;

-- Query 8 – HAVING
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

-- Query 9 – HAVING + AVG
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;

-- Query 10 – Business Scenario
SELECT department, COUNT(*) AS employee_count, SUM(salary) AS total_salary, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING employee_count >= 3
ORDER BY total_salary DESC;

-- Query 11
SELECT city, COUNT(*) AS employee_count
FROM employees
GROUP BY city
HAVING employee_count > 2;

-- Query 12
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC
LIMIT 1;


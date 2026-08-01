/* 
-- employees
emp_id
emp_name
department_id
salary
hire_date
city

-- departments
department_id
department_name
location
manager_name
*/

-- Query 1
WITH avg_salary AS (
    SELECT AVG(salary) AS average_salary
    FROM employees
)

SELECT e.emp_name, e.salary
FROM employees e
CROSS JOIN avg_salary a
WHERE e.salary > a.average_salary;

-- Query 2
WITH emp_count AS (
    SELECT department_id, COUNT(emp_id) AS employee_count
    FROM employees
    GROUP BY department_id
)

SELECT department_id, employee_count
FROM emp_count
WHERE employee_count > 3;

-- Query 3
SELECT emp_name, salary,
ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num
FROM employees;

-- Query 4
SELECT emp_name, salary,
RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Query 5
SELECT emp_name, salary,
DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Query 6
SELECT emp_name, department_id, salary,
RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS department_rank
FROM employees;

-- Query 7
WITH ranked_employees AS (
    SELECT emp_name, department_id, salary,
    ROW_NUMBER() 
    OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)

SELECT department_id, emp_name, salary
FROM ranked_employees
WHERE salary_rank = 1;

-- Query 8
WITH ranked_employees AS (
    SELECT emp_name, department_id, salary,
    ROW_NUMBER() 
    OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)

SELECT *
FROM ranked_employees
WHERE salary_rank <= 2;

-- Query 9
WITH dept_avg AS (
    SELECT department_id,
           AVG(salary) AS average_salary
    FROM employees
    GROUP BY department_id
)

SELECT e.emp_name,
       e.salary,
       e.department_id,
       d.average_salary
FROM employees e
JOIN dept_avg d
    ON e.department_id = d.department_id
WHERE e.salary > d.average_salary;

-- Query 10
WITH ranked_salary AS (
    SELECT emp_name, department_id, salary,
    DENSE_RANK() 
    OVER(
        ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)

SELECT department_id, emp_name, salary
FROM ranked_salary
WHERE salary_rank = 3; 
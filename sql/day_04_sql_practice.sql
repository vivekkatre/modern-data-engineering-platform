/*
# employees
emp_id
emp_name
department_id
salary
hire_date
city

# departments
department_id
department_name
location
manager_name
*/

-- Query 1 – INNER JOIN
SELECT emp_name, department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;

 -- Query 2 – INNER JOIN + Table Aliases
SELECT emp_name, department_name, salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY salary DESC;

-- Query 3 – LEFT JOIN
SELECT emp_name, department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;

-- Query 4 – LEFT JOIN (Business Scenario)
SELECT emp_name, city
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_id IS NULL;

-- Query 5 – RIGHT JOIN
SELECT department_name, emp_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

-- Query 6 – FULL OUTER JOIN
SELECT emp_name, department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id;

-- Query 7 – INNER JOIN + WHERE
SELECT emp_name, department_name, salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE department_name = 'IT'
AND salary > 70000;

-- Query 8 – INNER JOIN + ORDER BY
SELECT emp_name, department_name, hire_date
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY department_name ASC, hire_date DESC;

-- Query 9 – LEFT JOIN + Aggregate
SELECT department_name, COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name

-- Query 10 – Departments Without Employees
SELECT d.department_name, d.location , d.manager_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE emp_id IS NULL;

-- Bonus Challenge (Interview Style)
-- Query 11
SELECT emp_name, department_name, salary
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
ORDER BY salary DESC
LIMIT 3;

-- Query 12
SELECT department_name, AVG(salary) as average_salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
GROUP BY department_name
HAVING AVG(salary) > 70000
ORDER BY average_salary DESC;
/* -- employees
emp_id
emp_name
department
salary
hire_date
city 
*/

-- Query 1
SELECT emp_name, department, salary
FROM employees
WHERE department = 'IT'
AND salary > '60000';

-- Query 2
SELECT emp_name, city
FROM employees
WHERE city = 'Delhi'
    OR city = 'Mumbai';

-- Query 3
SELECT emp_name, department
FROM employees
WHERE department <> 'HR';

-- Query 4
SELECT emp_name, salary
FROM employees
WHERE salary BETWEEN 50000 AND 80000;

-- Query 5
SELECT emp_name, hire_date
FROM employees
WHERE hire_date BETWEEN '2021-01-01' AND '2023-12-31';

-- Query 6
SELECT emp_name, department
FROM employees
WHERE department IN ('IT', 'Finance', 'Sales');

-- Query 7
SELECT emp_name
FROM employees
WHERE emp_name LIKE 'S%';

-- Query 8
SELECT emp_name
FROM employees
WHERE emp_name LIKE '%n';

-- Query 9
SELECT emp_name
FROM employees
WHERE emp_name LIKE '%an%';

-- Query 10
SELECT emp_name, salary
FROM employees
ORDER BY salary DESC, emp_name ASC;

-- Query 11
SELECT emp_name, salary
FROM employees
ORDER BY salary DEC
LIMIT 3;

-- Query 12
SELECT  emp_name, department, salary, city
FROM employees
WHERE (
    department = 'IT' OR department = 'Finance'
    )
AND (
    salary BETWEEN '50000' AND '90000'
)
AND (
    city != 'Delhi'
)
ORDER BY salary DESC;

-- Query 13
SELECT emp_name
FROM employees
WHERE (
    emp_name LIKE 'A%' OR emp_name LIKE 'S%'
)
AND (
    salary > '70000'
)
AND (
    hire_date > '2022-01-01'
)
ORDER BY hire_date DESC;
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

-- Query 1
SELECT e.emp_name, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
);

-- Query 2
SELECT e.emp_name, e.hire_date
FROM employees e
WHERE e.hire_date > (
    SELECT MAX(e2.hire_date)
    FROM employees e2
    WHERE e2.department_id = 2
);

-- Query 3
SELECT e.emp_name, e.department_id, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);

-- Query 4
SELECT DISTINCT d.department_name
FROM departments d
INNER JOIN employees e
ON d.department_id = e.department_id
WHERE e.salary > 90000;

-- Query 5
SELECT e.city AS location
FROM employees e

UNION

SELECT d.location
FROM departments d;

-- Query 6
SELECT e.city AS location
FROM employees e

UNION ALL

SELECT d.location
FROM departments d; -- Duplicate values are allowed.

-- Query 7
SELECT e.city
FROM employees e

INTERSECT

SELECT d.location
FROM departments d;


-- Query 8
SELECT e.city
FROM employees e

EXCEPT

SELECT d.location
FROM departments d;

-- Query 9
SELECT e.emp_name, e.salary
FROM employees e
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
);

-- Query 10
SELECT d.department_name, AVG(e.salary) AS average_salary
FROM departments d
INNER JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > (
    SELECT AVG(e2.salary)
    FROM employees e2
);

-- Query 11
SELECT e.emp_name
FROM employees e
WHERE e.department_id in (
    SELECT e2.department_id
    FROM employees e2
    GROUP BY e2.department_id
    HAVING COUNT(*) > 5
);

-- Query 12
SELECT e.emp_name
FROM employees e
WHERE e.department_id in (
    SELECT d.department_id
    FROM departments d
    WHERE d.manager_name = "John Smith"
);

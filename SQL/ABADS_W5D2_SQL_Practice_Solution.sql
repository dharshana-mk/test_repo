-- Q1 - Which employees have more than 2 children
-- SELECT dependents.employee_id, count(dependents.employee_id) from dependents INNER Join employees on dependents.employee_id = employees.employee_id GROUP By dependents.employee_id;


 
-- Q2 - Where are most of the employees based out of (Location)
-- SELECT locations.city, count(locations.city) FROM employees 
-- INNER JOIN (departments INNER JOIN locations ON locations.location_id=departments.location_id) 
-- ON employees.department_id=departments.department_id 
-- GROUP By locations.city;


-- Q3 - What is the average salary of the last 10 employees who joined the company
-- SELECT avg(salary) from employees order by hire_date Desc LIMIT 10;



-- Q4 - How many of your employees are from London
-- SELECT locations.city, count(locations.city ) FROM employees 
-- INNER JOIN (departments INNER JOIN locations ON locations.location_id=departments.location_id) 
-- ON employees.department_id=departments.department_id Where locations.city = 'London'



-- Q5 - Which department has the most employees
-- SELECT department_id, count(department_id) FROM employees GROUP BY department_id order by count(department_id) DESC;

-- If you want to delve deeper into the department names, feel free to join the appropriate table



-- Q6 - Which department makes the least amount of money 
-- SELECT department_id,avg(salary) from employees GROUP BY department_id order by avg(salary) Desc;








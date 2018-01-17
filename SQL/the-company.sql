--https://www.hackerrank.com/challenges/the-company/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT
    employee.company_code, 
    company.founder, 
    COUNT(DISTINCT(lead_manager_code)), 
    COUNT(DISTINCT(senior_manager_code)),
    COUNT(DISTINCT(manager_code)),
    COUNT(DISTINCT(employee_code))
FROM
    employee
JOIN
    company
ON
    employee.company_code = company.company_code
GROUP BY
    employee.company_code, company.founder
ORDER BY
    employee.company_code

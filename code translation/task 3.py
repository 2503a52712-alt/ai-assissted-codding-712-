-- SQL
SELECT name, salary
FROM employees
WHERE salary > 50000;

# Python with Pandas
import pandas as pd

employees = pd.DataFrame({
    "name": ["Asha", "Ravi", "Mina", "John"],
    "salary": [60000, 45000, 75000, 50000]
})

result = employees.loc[
    employees["salary"] > 50000,
    ["name", "salary"]
]

print(result)
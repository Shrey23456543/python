Employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "Sales", "salary": 60000},
    {"name": "Charlie", "department": "Sales", "salary": 55000},
    {"name": "David", "department": "IT", "salary": 70000}
]

sales_Employees = [emp["name"].upper() for emp in Employees if emp["department"] == "Sales"]

print(sales_Employees)

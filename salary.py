salary=int(input("Enter salary:"))
if salary>=50000:
    DA=salary/10
    HRA=salary/12
    new_salary=salary+DA+HRA
    print("new salary after DA and HRA will be",new_salary)

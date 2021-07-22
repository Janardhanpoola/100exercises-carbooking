emp={'emp_no':100,
    'emp_name':"raj",
    'emp_sal':1000,
    'emp_adr':"Mumbai"
}

Employee_number=emp['emp_no']
Employee_name=emp['emp_name']
Employee_salary=emp['emp_sal']
Employee_address=emp['emp_adr']

res='Employee_number:{}\nEmployee_name:{}'.format(Employee_number,Employee_name)

print(res)
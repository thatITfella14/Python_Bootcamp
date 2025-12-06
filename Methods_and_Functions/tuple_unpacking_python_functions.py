work_hours = [("Abby",100),("Billy",400),("Cassie",800)]

# below is how you can use tuple unpacking to get the values using a for loop:

for employee, hours in work_hours:
    print(employee,hours)

print()

# below is how you can use tuple unpacking to get the values using a function, however, we're wanting to see who worked the most hours:

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    return (employee_of_month,current_max)

result = employee_check(work_hours)

print(result)
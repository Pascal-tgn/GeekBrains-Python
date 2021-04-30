total_salaries = 0
with open(r'e3_employees.txt', 'r') as my_file:
    my_employees = my_file.readlines()
    for person_data in my_employees:
        name, salary = person_data.split()
        if float(salary) < 20000:
            print(f"{name}'s salary is low: {salary}")
        total_salaries += float(salary)
average_salary = total_salaries / len(my_employees)
print(f"\nAverage salary of all employees is: {average_salary}")

# First task
# ---------------------------------------------------------------------------------------------------------------------
current_date = '05.17.2016'
lst = current_date.split('.')
month = int(lst[0])
days = int(lst[1])
year = int(lst[2])
print('%d.%d.%d' % (days, month, year))

# Second Task
# ---------------------------------------------------------------------------------------------------------------------
student = 'Mark Zuckerberg'
lst = student.split(' ')
name = lst[0]
surname = lst[1]
print('%s %s' % (surname, name))

# Third Task
# ---------------------------------------------------------------------------------------------------------------------
snake_style = 'employee_first_name'
lst = snake_style.split('_')
employee = lst[0]
first = lst[1]
name = lst[2]
print('%s%s%s' % (employee.capitalize(), first.capitalize(), name.capitalize()))

# Fourth Task
# ---------------------------------------------------------------------------------------------------------------------

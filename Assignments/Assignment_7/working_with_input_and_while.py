# Gen Li 
# 1060038
# Sunday, October 18, 2020 at 11:59 pm
# MSITM 6341

# Assignment #7
# Assignment Title :Workint with input and while

print('Please input the name and monthly income for each person.')
print('Please enter ‘quit’ in the name field to stop the user input.')
print()
name_salary = {}
formatted_marks = '${:.2f}'

active = True
while active:
  name_input = input('Please type in the name: ')
  if name_input == 'quit':
      break
      #active = False
  salary_input = input('Please type in the salary: ')
  salary = float(salary_input)
  name_salary[name_input.title()] = salary

print()
print('Names and salaries input end, Please see the results below with sorted name: ')
print()
print('='*50)
print("Name\t\t\tSalary")
print('-'*50)

for key, value in sorted(name_salary.items()):
  print(key+'\t\t\t'+formatted_marks.format(value))
print('='*50)

max_salary = max(name_salary, key=name_salary.get)
print(
    f'{max_salary} makes the hightest monthly income {formatted_marks.format(name_salary[max_salary])}')
min_salary = min(name_salary, key=name_salary.get)
print(
    f'{min_salary} makes the lowest monlthly income {formatted_marks.format(name_salary[min_salary])}')
print('-'*50)

# Gen Li
# 1060038
# Sunday, September 20, 2020 at 11:59 pm
# MSITM 6341

# Assignment #4
# Assignment Title :Workint with for loop

first_names = ['tina', 'andrew', 'matthew', 'patrick', 'adam',
               'andrea', 'cynthia', 'russell', 'robert', 'katherine']
last_names = ['rogers', 'phillips', 'howard', 'cook',
              'gonzales', 'white', 'long', 'james', 'foster', 'martin']
scores = [92.00, 93.50, 90.00, 87.80, 91.30, 88.00, 85.00, 81.40, 94.50, 96.00]

#1. Print the entire first name, last name using for loop
print('The first name list:')
for first_name in first_names:
  print(first_name.title())
print()
print('The last name list:')
for last_name in last_names:
  print(last_name.title())
print()

#2. Print the first name and last name on the same output line as formatted below (first letter must be capital).
print('Student Full Name: ')
print('------------------')
for i in range(len(first_names)):
  print(first_names[i].title()+' '+last_names[i].title())
print()

#3. Print the first name and last name in capital letter on the same output line as formatted below
print('Student Full Name: ')
print('------------------')
for i in range(len(first_names)):
  print(first_names[i].upper()+' '+last_names[i].upper())
print()

#4. Remove 3rd item in the all three list.
first_names.pop(2)
last_names.pop(2)
scores.pop(2)

#5.Add a new student information (first name, last name and score) on 2nd index for each of the three list.Print the first name, last name and score on the same output line as formatted below
first_names.insert(2, 'macus')
last_names.insert(2, 'baldwin')
scores.insert(2, 87.00)
print('Student Full Name and Score: ')
print('----------------------------')
for j in range(len(first_names)):
    print(
        f'{first_names[j].title()} {last_names[j].title()} - {"{:.2f}".format(scores[j])}')
print()

#6. Sort the first name list and print each first name in one line. Print a heading as “List of All Students first name: ”
print('List of All Student First Name(Sorted):')
print('---------------------------------------')
first_names.sort()
for sorted_first_name in first_names:
  print(sorted_first_name.title())
print()

#7. Create a tuple with first five elements of student first name list and print that tuple
turple_names = tuple((first_names[:5]))
print(turple_names)

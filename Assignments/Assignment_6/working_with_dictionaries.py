# Gen Li
# 1060038
# Sunday, October 11, 2020 at 11:59 pm
# MSITM 6341

# Assignment #6
# Assignment Title :Workint with dictionary


# List of Students
student_names = ['Mike', 'Sarah', 'Matthew', 'Smith','Melanie', 'Renjith', 'Rahul', 'Mark', 'Rebeka', 'Jenna']

# List of Students Mark
students_math_marks =      [91.99, 94.43, 89, 85.23, 90.31, 88, 78.6, 92, 94.35, 80.72]
students_english_marks =   [83.56, 95.34, 83, 90.44, 88.32, 95, 97.7, 91, 95.54, 89.32]
students_physics_marks =   [92.19, 89.51, 90, 88.55, 89.45, 97, 89.8, 87, 81.72, 93.54]
students_chemistry_marks = [89.64, 87.63, 98, 94.66, 93.78, 85, 86.9, 95, 84.81, 91.86]

#Dictionary for storing student name and marks
student_info = {}

# Create a list of total mark
students_total_marks = []
i = 0
formatted_marks = '{:.2f} \t\t\t'
for student in student_names:
    students_total_marks.append(
        students_math_marks[i] +
        students_english_marks[i] +
        students_physics_marks[i] +
        students_chemistry_marks[i])
    #print(formatted_marks.format(students_total_marks[i]))
    i += 1

#Create empty dictonary of student mark,loop through every student and add class marks in the dictionary

student_marks = {}
student_marks_list = []
i = 0
for student in student_names:
  student_marks['math'] = students_math_marks[i]
  student_marks['english'] = students_english_marks[i]
  student_marks['physics'] = students_physics_marks[i]
  student_marks['chemistry'] = students_chemistry_marks[i]
  student_marks['total_marks'] = students_total_marks[i]
#print(student_marks)

  student_info = {student: student_marks}
  student_info[student] = student_marks

  print(student_info)

  i += 1

  #Put student name and mark dictionalry in the root dictionary


#print(student_info)
#Print out header
print("="*90)
ctr = 0
print("Name\t\t\tMath\t\t\tEnglish\t\t\tPhysics\t\t\tChemistry\t\tTotal Marks")
print("-"*90)

for keys, values in student_info.items():
  print(keys)
  print(values)

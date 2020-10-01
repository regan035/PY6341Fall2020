# Full Name: Gen Li
# Student ID: 1060038
# Exam Date: September 29, 2020 at 08:00pm
# Due Date: September 29, 2020 at 11:59pm
# MSITM 6341
# Mid Term Exam - Online

#========================= Instructions =========================#
#
# Welcome to Midterm Python Exam. This exam must be turned in 4 hours.
# There are 6 questions and each question have 32 points (32 X 6 = 192).
# Proper tabular formatting has 8 points
# Please add necessary comments and styling.
# Problem statement: There are ten students and their marks are given in the problem statement
# Do not change the student’s name, their marks and its order.
# Assumption is all students have unique/different total marks (each student’s total mark is unique)
# You need to solve the below six requirements using python code covered in the last five sessions.
# Should not hardcode output values
#
#================ Solve the Following Questions =================#
#
# 1. Add each student’s total mark and store it in a list.
# 2. Print Each student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab.
# 3. Print Highest scored student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab.
# 4. Print Lowest scored student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab.
# 5. Print all student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab
#    Student's Name start with “M” and English mark between 83 and 88.
# 6. Print all student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab
#    Student's Name ends with “h” and Math mark higher than 90 or Physics mark > 95
#
#--------------------------------------------------------------#
#
# Tip for using and & or condition in a if condition
# if (<common condition> and (<first_or_condition> or <second_or_condition>)):
# example: if (age > 18 and (us_citizen == True or canada_citizen == True))
#
#==============================================================#


# List of Students
student_names = ['Mike', 'Sarah', 'Matthew', 'Smith',
                 'Melanie', 'Renjith', 'Rahul', 'Mark', 'Rebeka', 'Jenna']

# List of Students Mark
students_math_marks = [91.99, 94.43, 89,
                       85.23, 90.31, 88, 78.6, 92, 94.35, 80.72]
students_english_marks = [83.56, 95.34, 83,
                          90.44, 88.32, 95, 97.7, 91, 95.54, 89.32]
students_physics_marks = [92.19, 89.51, 90,
                          88.55, 89.45, 97, 89.8, 87, 81.72, 93.54]
students_chemistry_marks = [89.64, 87.63, 98,
                            94.66, 93.78, 85, 86.9, 95, 84.81, 91.86]

students_total_marks = []

# 1. Add each student’s total mark and store it in a list.
print('Question#1')
students_total_marks = []
i = 0
for student_name in student_names:
  total_mark = students_math_marks[i]+students_english_marks[i] + \
      students_physics_marks[i]+students_chemistry_marks[i]
  i += 1
  students_total_marks.append(total_mark)

print(students_total_marks)
# 2. Print Each student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab.
print('Question#2')
subjects = ['Name', 'Math', 'English', 'Physics', 'Chemistry', 'Total Mark']
i = 0
for subject in subjects:
  print(subject, end="\t")
print()
for student_name in student_names:
  print(student_names[i], '\t', students_math_marks[i], '\t', students_english_marks[i], '\t',
        students_physics_marks[i], '\t', students_chemistry_marks[i], '\t', students_total_marks[i])
  i += 1
  print()

# 3. Print Highest scored student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab.
print('Question #3')
max = (max(students_total_marks))
imax = students_total_marks.index(max)
print(student_names[imax], '\t', students_math_marks[imax], '\t', students_english_marks[imax],
      '\t', students_physics_marks[imax], '\t', students_chemistry_marks[imax], '\t', students_total_marks[imax])
print()
# 4. Print Lowest scored student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab.
print('Question#4')
min = (min(students_total_marks))
imin = students_total_marks.index(min)
print(student_names[imin], '\t', students_math_marks[imin], '\t', students_english_marks[imin],
      '\t', students_physics_marks[imin], '\t', students_chemistry_marks[imin], '\t', students_total_marks[imin])
print()
# 5. Print all student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated by tab
#    Student's Name start with “M” and Enlish mark between 83 and 88.
print('Question#5')
for subject in subjects:
  print(subject, end="\t")
print()
index_new = []
for student_name in student_names:
    if student_name[0] == 'M':
      im = (student_names.index(student_name))
      index_new.append(im)

new_name = []
new_math = []
new_eng = []
new_pyh = []
new_chem = []
new_total = []

for i in index_new:
 new_name.append(student_names[i])
 new_math.append(students_math_marks[i])
 new_eng.append(students_english_marks[i])
 new_pyh.append(students_physics_marks[i])
 new_chem.append(students_chemistry_marks[i])
 new_total.append(students_total_marks[i])

for j in new_eng:
  if (j >= 83 and j <= 88):
    #print(j)
    #print(new_eng.index(j))
    print(new_name[new_eng.index(j)], '\t', new_math[new_eng.index(j)], '\t', new_eng[new_eng.index(
        j)], '\t', new_pyh[new_eng.index(j)], '\t', new_chem[new_eng.index(j)], '\t', new_total[new_eng.index(j)])
    print()

# 6. Print all student’s Name, Math, English, Physics, Chemistry and Total Mark in a single line, columns separated [by tab
#    Student's Name ends with “h” and Math mark higher than 90 or Physics mark > 95
print('Question#6')
for subject in subjects:
  print(subject, end="\t")
print()
index_new = []
for student_name in student_names:
    if student_name[-1] == 'h':
      ih = (student_names.index(student_name))
      index_new.append(ih)

new_name_h = []
new_math_h = []
new_eng_h = []
new_pyh_h = []
new_chem_h = []
new_total_h = []

for i in index_new:
 new_name_h.append(student_names[i])
 new_math_h.append(students_math_marks[i])
 new_eng_h.append(students_english_marks[i])
 new_pyh_h.append(students_physics_marks[i])
 new_chem_h.append(students_chemistry_marks[i])
 new_total_h.append(students_total_marks[i])


for k in new_math_h:
  if (k > 90):
    print(new_name_h[new_math_h.index(k)], '\t', new_math_h[new_math_h.index(k)], '\t', new_eng_h[new_math_h.index(
        k)], '\t', new_pyh_h[new_math_h.index(k)], '\t', new_chem_h[new_math_h.index(k)], '\t', new_total_h[new_math_h.index(k)])
    print()

for l in new_pyh_h:
  if (l > 95):

    print(new_name_h[new_pyh_h.index(l)], '\t', new_math_h[new_pyh_h.index(l)], '\t', new_eng_h[new_pyh_h.index(
        l)], '\t', new_pyh_h[new_pyh_h.index(l)], '\t', new_chem_h[new_pyh_h.index(l)], '\t', new_total_h[new_pyh_h.index(l)])

# Gen Li
# 1060038
# Sunday, October 4, 2020 at 11:59 pm
# MSITM 6341

# Assignment #5
# Assignment Title :Workint with if statement

full_name = 'Gen Li'

full_name_a = []
full_name_b = []
i = 0
i < len(full_name)
print('My name is '+full_name.title())
print()
print('---------------------------')
print()
for char in full_name:

  if char == char.upper():
    full_name_a.append(char.lower())
    full_name_b.append(str(ord(char.lower())))

  else:
    full_name_a.append(char.upper())
    full_name_b.append(str(ord(char.upper())))

  print(f"ASCII value of {full_name_a[i]} is {ord(full_name_a[i])}")
  i += 1

j = 0
for char1 in full_name_a:
  print(char1, end='-')
print()
for char2 in full_name_b:
  print(char2, end='-')



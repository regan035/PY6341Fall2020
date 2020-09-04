# Gen Li
# 1060038
# Sunday, September 6th, 2020 at 11:59 pm
# MSITM 6341

# Assignment #2
# Assignment Title: String and Numeric Functions

#Define two numerical variable
var1 = 20
var2 = 40

#Writing mathematic logic
sum = var1 + var2
result = sum/7.6
formated_result = "{:,.2f}".format(result)

#Print out results
print('============================')
print('Result Dashboard')
print('----------------------------')
print('Value 1: ' + str(var1))
print('\n')
print('Value 2: ' + str(var2))
print('----------------------------')
print('Total summary: ' + str(sum))
print('Result: $'+str(formated_result))
print('============================')

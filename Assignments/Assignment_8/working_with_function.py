# Gen Li 
# 1060038
# Sunday, October 25, 2020 at 11:59 pm
# MSITM 6341

# Assignment #8
# Assignment Title :Workint with functions
city_temp_dict={}
active = True
while active:
  city_name=input('Please type in the city name: ')
  if city_name.lower() == 'done':
    break
  city_temp=input('please type in the temperature: ')
  int_city_temp = int(city_temp)
  city_temp_dict[city_name.title()]=int_city_temp

def classify_temperatur(float_city_temp):
  if float_city_temp>100:
    temp_cla = 'Very Hot weather'
  if float_city_temp<=100:
    temp_cla = 'Hot weather'
  if float_city_temp<=90:
    temp_cla = 'Warm'
  if float_city_temp<=80:
    temp_cla = 'Good weather'
  if float_city_temp<=70:
    temp_cla = 'Cold'
  if float_city_temp<=50:
    temp_cla = 'Very Cold'
  if float_city_temp<=32:
    temp_cla = 'Freezing Weather'
  return(temp_cla)

print('='*80)  
print('City Name\t\t\tTemperature\t\tTemperature classification')
print('='*80)
for key,value in (city_temp_dict.items()):
  print(f'{key} \t\t\t {str(value)} \t\t\t {classify_temperatur(value)}')
print('='*80)
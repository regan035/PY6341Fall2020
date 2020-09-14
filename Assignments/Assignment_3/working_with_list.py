# Gen Li
# 1060038
# Sunday, September 13th, 2020 at 11:59 pm
# MSITM 6341

# Assignment #3
# Assignment Title: Working with lists

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Anthonio', 'San Diego', 'Dallas', 'San Jose']

population_list = [8336817, 3979576, 2693976, 2320268,
                   1680992, 1680992, 1547253, 1423851, 1343573, 1021795]

#1.Print the entire city list and population list in two separate lines.
print(city_list)
print("\n")
print(population_list)
print("\n")

#2. Print the 3rd item followed by its population
third_pop = population_list[2]
print(
    f"The 3rd city in the list is {city_list[2]}. The population is {third_pop:,}.")
print("\n")

#3. Print the last item in the city list followed by its population.
last_pop = population_list[-1]
print(
    f"The last city in the list is {city_list[-1]}. The population is {last_pop:,}.")
print("\n")

#4. Add a new city in 6th item position of city list and the new cities population on the population listexactly on 6th position. (now both lists will have 11 items)
city_list.insert(5, 'Austin')
population_list.insert(5, 978908)

#5. Print the list of all cities
print(city_list)
print("\n")
#6. Print the list of all population
print(population_list)
print("\n")
#7. Remove the 3rd item from city list and the corresponding population item from population list.
city_list.pop(2)
population_list.pop(2)

#8. Print the both list in two separate line.
print(city_list)
print("\n")
print(population_list)
print("\n")

#9. Print both sorted list in a separate line
print((sorted(city_list)), (sorted(population_list)))
print("\n")

#10. Double the population of the 2nd item in the population list

new_pop = population_list[1]*2
print(f"The double of 2nd item in population list is {new_pop:,}.")

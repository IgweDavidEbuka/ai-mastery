# Day 2: 30 Days of Python Programming

# Exercises: Level 1
first_name = 'Ebuka'
last_name = 'Igwe'
full_name = 'Chukwuebuka David Igwe'
country = 'Nigeria'
city = 'PH'
age = 23
year = 2003
is_married = False
is_true = True
is_light_on = False

weight, height, complexion, gender = "75kg", "5'11", "Dark", "Male"

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))

print(len(first_name))
print(len(last_name))

if len(first_name) > len(last_name):
    print("X")
else:
    print('Y')

num_one, num_two = 5, 4
variable_total = num_one + num_two
variable_diff = num_two - num_one
variable_product = num_two * num_one
variable_division = num_one / num_two
variable_floor_division = num_one // num_two
variable_remainder = num_two % num_one
variable_exp = num_one ** num_two

r = float(input('What is the radius? '))
area_of_circle = round(3.142 * r * r, 2)
circum_of_circle = round(2 * 3.142 * r, 2)
print((area_of_circle, circum_of_circle))

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("What is your country? ")
age = input("What is your age? ")

help('keywords')
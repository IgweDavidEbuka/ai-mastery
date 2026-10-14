# Boolean
# The usual true or false

# Assignment operators : The usual +, -, //, /, etc

age = int(23)
height = float(180)
compl = 1 + 1j

# Triangle #
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_triangle =  round(0.5 * base * height)
print("The area of the triangle is",area_triangle) 

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perm = (a + b + c)
print("The perimeter of the triangle is", perm)

# Rectangle #

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area_rect = length * width
perimeter = 2 * (length + width)

print(f'The area of the rectangle is {area_rect}. The perimeter is {perimeter}')

# Circle #

rad = float(input("Enter radius: "))
pi = 3.14
circle_area = round(pi * rad * rad, 2)
circle_perm = round(2 * pi * rad, 2)
print(f'The area of the circle is {circle_area}. The perimeter is {circle_perm}')

# Math #

p1 = (2, 2)
p2 = (6, 10)

x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]

m = round(y2 - y1 / x2 - x1, 2)
ecud = round(((x2 - x1)**2 + (y2 - y1)** 2)**0.5, 2)
print(f'The Slope is {m} and the Euclidean Distance is {ecud}')

x = -3
y = x ** 2 + 6*x + 9
print(y)

#Falsey comparison statement#

x = 'python'
y = 'dragon'

print(len(x) == len(y))

age = float(input("Enter your age: "))
age_seconds = age * 365 * 24 * 60 * 60
print(f'You have lived for {age_seconds} seconds.')

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
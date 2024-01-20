# Question Number 1 Solution

# Taking input from the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating addition
addition_result = num1 + num2
print("Addition : ", num1, "+", num2, "=", addition_result)

# Calculating division
division_result = num1 / num2
print("Division : ", num1, "/", num2, "=", division_result)

# Calculating power
power_result = num1 ** num2
print("Power : ", num1, "^", num2, "=", power_result)

# Calculating floor division
floor_division_result = num1 // num2
print("Floor : ", num1, "//", num2, "=", floor_division_result)

# Question Number 2 Solution

# Taking input from the user for length and height
length = float(input("Enter the length (base) of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculating the area of the triangle
area = 0.5 * length * height

# Printing the result
print(f"The area of the triangle is: {area}")

# Question Number 3 Solution


# Taking input from the user for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Printing the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Question Number 4 Solution

# Integer
integer_number = 42

# Floating-point
float_number = 3.14

# String
string_value = "Hello, World!"

# Boolean
boolean_value = True

# List
list_values = [1, 2, 3, "a", "b", "c"]

# Tuple
tuple_values = (4, 5, 6, "x", "y", "z")

# Dictionary
dictionary_values = {'name': 'ayesha', 'age': 15, 'city': 'Karachi'}

# Set
set_values = {7, 8, 9, "p", "q", "r"}

# NoneType
none_value = None

# Print the values and their types
print("The data type of", integer_number, "is", type(integer_number))
print("The data type of", float_number, "is", type(float_number))
print("The data type of", string_value, "is", type(string_value))
print("The data type of", boolean_value, "is", type(boolean_value))
print("The data type of", list_values, "is", type(list_values))
print("The data type of", tuple_values, "is", type(tuple_values))
print("The data type of", dictionary_values, "is", type(dictionary_values))
print("The data type of", set_values, "is", type(set_values))
print("The data type of", none_value, "is", type(none_value))

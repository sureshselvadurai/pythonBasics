# Variable assignment
x = 5
y = "Hello, Python!"

# Printing variables
print("x:", x)
print("y:", y)

# Numeric types
integer_variable = 10
float_variable = 3.14

# Strings
string_variable = "Python is powerful!"

# Lists
list_variable = [1, 2, 3, 4, 5]

# Tuples
tuple_variable = (1, "two", 3.0)

# Dictionaries
dict_variable = {"key1": "value1", "key2": 42}

# Conditional Statements (if, elif, else)
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# For loop
print("Numbers from 1 to 4:")
for num in range(1, 5):
    print(num)

# While loop
print("Counting from 0 to 4:")
count = 0
while count < 5:
    print(count)
    count += 1

# Exception Handling (try, except)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)

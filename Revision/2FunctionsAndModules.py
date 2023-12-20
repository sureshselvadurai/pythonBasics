# Function definition
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"


# Function calling
user_name = "Alice"
greeting_message = greet(user_name)
print(greeting_message)


# Modules and Packages
# Creating a simple module named mymodule.py

# mymodule.py
def add_numbers(a, b):
    """This function adds two numbers."""
    return a + b


def subtract_numbers(a, b):
    """This function subtracts b from a."""
    return a - b


# Using the module in another file
# main.py
# import mymodule

# result_add = mymodule.add_numbers(5, 3)
# print("Addition Result:", result_add)

# result_subtract = mymodule.subtract_numbers(8, 3)
# print("Subtraction Result:", result_subtract)

# Chapter 10: Best Practices and Advanced Concepts

# Code Style and PEP 8

# Good code style
def calculate_sum(a, b):
    return a + b

# Following PEP 8
def calculate_sum_pep8(a, b):
    return a + b

# Explanation: PEP 8 is the style guide for Python code. It provides conventions for writing clean and readable code.
# In the example, `calculate_sum_pep8` adheres to PEP 8 by using underscores to separate words in the function name.

# Advanced Concepts

# Generators and Iterators
def simple_generator():
    yield 1
    yield 2
    yield 3

# Using a generator in a for loop
for value in simple_generator():
    print("Generator Value:", value)

# Explanation: Generators are a concise way to create iterators in Python. They use the `yield` keyword to produce a series of values.
# In the example, `simple_generator` is a generator function, and the `for` loop iterates over its values.

# Context Managers
class SampleContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

# Using a context manager with the 'with' statement
with SampleContextManager():
    print("Inside the context")

# Explanation: Context managers are used for resource management. The `with` statement ensures proper setup and cleanup.
# In the example, `SampleContextManager` is a simple context manager. The `with` statement handles entering and exiting the context.

# Metaclasses
class SampleMetaclass(type):
    def __new__(cls, name, bases, dct):
        dct['custom_attribute'] = 42
        return super().__new__(cls, name, bases, dct)

# Using a metaclass to create a class
class MyClass(metaclass=SampleMetaclass):
    pass

# Accessing the custom attribute
print("Custom Attribute Value:", MyClass.custom_attribute)

# Explanation: Metaclasses are classes for classes. They control the creation of classes. In the example, `SampleMetaclass` adds a custom attribute to classes created with it.

# Decorators
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()

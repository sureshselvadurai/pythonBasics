# Chapter 9: Testing and Debugging

# Writing Unit Tests with unittest

import unittest

# Simple function to be tested
def add_numbers(a, b):
    return a + b

# Test case class
class TestAddition(unittest.TestCase):

    # Test method
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -4), -6)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(2, -7), -5)

# Running the tests
if __name__ == '__main__':
    unittest.main()

# Basic Debugging Techniques

# Using print statements for debugging
def divide_numbers(a, b):
    print(f"Dividing {a} by {b}")
    result = a / b
    print("Result:", result)
    return result

# Uncomment the following lines to see the debug output
# divide_numbers(10, 2)
# divide_numbers(5, 0)  # Causes a ZeroDivisionError

# Using try-except for debugging
try:
    result = divide_numbers(5, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Using breakpoints and debugging tools
def multiply_numbers(a, b):
    result = a * b
    breakpoint()  # Set a breakpoint here
    return result

# Uncomment the following line to enable debugging
# multiply_numbers(3, 7)

# Chapter 6: Python Libraries and Frameworks

# Standard Library

# Working with Dates and Times
from datetime import datetime, timedelta

current_time = datetime.now()
print("Current time:", current_time)

one_day_later = current_time + timedelta(days=1)
print("One day later:", one_day_later)

# Working with the Operating System
import os

current_directory = os.getcwd()
print("Current directory:", current_directory)

# Third-Party Libraries

# NumPy - Numerical Computing
import numpy as np

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

result_array = array_a + array_b
print("NumPy Array Addition Result:", result_array)

# pandas - Data Analysis and Manipulation
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# requests - HTTP Library
import requests

response = requests.get("https://www.example.com")
print("\nHTTP Response Status Code:", response.status_code)

# matplotlib - Data Visualization
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

plt.plot(x_values, y_values)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

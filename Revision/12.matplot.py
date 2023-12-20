# Chapter 13: Advanced Topics (Data Visualization)

# Data Visualization with Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Generating data for plotting
x_values = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y_values_sin = np.sin(x_values)
y_values_cos = np.cos(x_values)

# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values_sin, label='sin(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x_values, y_values_cos, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Adding labels and title
plt.title('Sin(x) and Cos(x) Functions')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()

# Explanation:
# - Matplotlib is a popular library for data visualization in Python.
# - In this example, data is generated using NumPy and then plotted using Matplotlib.
# - Two functions (sin(x) and cos(x)) are plotted on the same graph with different styles.
# - Labels, title, legend, and grid are added for better presentation.


import matplotlib.pyplot as plt
import numpy as np

# Read values from a.dat file
data = np.loadtxt("a.dat")

# Extract x and y values using array slicing
x_values = data[:, 0].astype(int)
y_values = data[:, 1]

# Create a stem plot
plt.stem(x_values, y_values, linefmt='-', markerfmt='o', basefmt='')

# Add labels and title
plt.xlabel('n')
plt.ylabel('6 + 6n')
plt.title('Stem Plot of x(n) vs n')

# Display the plot
plt.show()

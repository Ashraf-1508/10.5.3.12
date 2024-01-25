import matplotlib.pyplot as plt
import numpy as np

# Generate data points using NumPy arrays
n_values = np.arange(0, 22)
y_values = 6 + 6 * n_values

# Create a stem plot
plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt='')

# Add labels and title
plt.xlabel('n')
plt.ylabel('6 + 6n')
plt.title('Stem Plot of x(n) vs n')

# Display the plot
plt.show()

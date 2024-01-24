import matplotlib.pyplot as plt

# Generate data points
n_values = list(range(0,22))
y_values = [6 + 6 * n for n in n_values]

# Create a stem plot
plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt=' ')

# Add labels and title
plt.xlabel('n')
plt.ylabel('6 + 6n')
plt.title('Stem Plot of 6+6n vs n')

# Display the plot
plt.show()

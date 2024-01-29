import matplotlib.pyplot as plt

# Read values from a.dat file
with open("a.dat", "r") as file:
    data = [line.split() for line in file]

# Extract x and y values
x_values = [int(row[0]) for row in data]
y_values = [float(row[1]) for row in data]

# Create a stem plot
plt.stem(x_values, y_values, linefmt='-', markerfmt='o', basefmt='')

# Add labels and title
plt.xlabel('n')
plt.ylabel('6 + 6n')
plt.title('Stem Plot of x(n) vs n')

# Display the plot
plt.show()


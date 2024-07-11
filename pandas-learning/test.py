import numpy as np
import matplotlib.pyplot as plt

# Data for the plots
x = np.arange(-10, 11)
y = x**2
y_2 = -y
y_3 = x + 2
y_4 = math.cos(x)

# Plotting the axes
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal line at y=0 (x-axis)
plt.axvline(0, color='black', linewidth=0.5)  # Vertical line at x=0 (y-axis)

# Plotting the other curves
plt.plot(x, y_3, label='y = x + 2')
plt.plot(x, y, label='y = x^2')
plt.plot(x, y_2, label='y = -x^2')

# Adding title and legend
plt.title("Représentation graphique de $y = x^2$ et de $y = -x^2$")
plt.legend()

# Displaying the plot
plt.show()

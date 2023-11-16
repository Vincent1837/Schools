import matplotlib.pyplot as plt
import numpy as np

# Create an array of L/R values from 0 to 1
L_over_R = np.linspace(0, 1, 100)

# Calculate total delay for each L/R value
total_delay = L_over_R * (1 / (1 - L_over_R) + 1 / 1)

# Create the plot
plt.plot(L_over_R, total_delay)
plt.xlabel('L/R')
plt.ylabel('Total Delay (D)')
plt.title('Total Delay vs. Traffic Intensity (L/R)')
plt.grid(True)

# Show the plot
plt.show()
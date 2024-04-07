import random
import matplotlib.pylab as plt
import keyboard
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

""" # Create a figure and axis
fig, ax = plt.subplots()

# Create an empty plot object which will be updated during the animation
line, = ax.plot([], [], lw=2)

# Set the axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Initialize function to generate the frames of the animation
def init():
    line.set_data([], [])
    return line,

# Define the function to update the plot for each frame
def update(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + frame*0.1)  # Varying phase to create animation effect
    line.set_data(x, y)
    return line, """



# 1.Generate a random permutation of 50 numbers ranging from 1 to 50.
data = [x for x in range(1, 51)]
random.shuffle(data)


figure = plt.figure(figsize=(14, 3))
axes = figure.subplots(1, 5)
titles = ["bubble sort", "insertion sort", "merge sort", "quick sort", "heap sort"]
for i in range(5):
    axes[i].set_title(titles[i])
    axes[i].bar(list(range(1, 51)), data)

# Create the animation
#ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, interval=10)

# Show the animation
plt.show()

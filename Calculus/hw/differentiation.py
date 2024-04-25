import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta = np.linspace(0, 14*np.pi, 1000)
r = np.sin(theta*(8/7))
ax.plot(theta, r, color='b')
plt.title("graph of sin(8x/7) for x in [0, 14pi]", color="red")
ax.grid(True)
plt.show()

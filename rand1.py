import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of particles
N = 1000

# Initialize particle positions (in polar coordinates)
r = np.zeros(N)
theta = np.random.uniform(0, 2*np.pi, N)

# Radial step size
dr = 0.01

# Initialize figure
fig, ax = plt.subplots()

# Perform the random walk
def update(num):
    ax.clear()
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')

    # Update the radial position with a random step
    global r
    r += np.random.uniform(-dr, dr, N)

    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot
    ax.plot(x, y, 'k.')

ani = animation.FuncAnimation(fig, update, frames=200, repeat=False)
plt.show()

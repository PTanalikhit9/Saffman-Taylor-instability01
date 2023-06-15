
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of particles and steps
N = 1000
steps = 500

# Initialize particle positions (in polar coordinates)
r = np.zeros(N)
theta = np.random.uniform(0, 2*np.pi, N)

# Radial step size and noise strength
dr = 0.01
noise_strength = 0.002

# External force pushing the particles outwards
force = 0.005

# Initialize figure
fig, ax = plt.subplots()

# Perform the random walk with branching
def update(num):
    ax.clear()
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')

    # Update the radial position with a random step and an external force
    global r
    r += np.random.normal(force, noise_strength, N)

    # Prevent particles from moving inwards
    r = np.maximum(r, 0)

    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot
    ax.plot(x, y, 'k.')

ani = animation.FuncAnimation(fig, update, frames=steps, repeat=False)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
D = 0.1  # Diffusion constant
N = 100  # Grid points
T = 500   # Time steps

# Initialization
u = np.zeros((N, N))
u[N//2, N//2] = 100  # A drop of fluid at the center

# Simulation
def step(u):
    u_new = u.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            u_new[i, j] = u[i, j] + D * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - 4*u[i, j])
    return u_new

# Animation
fig = plt.figure()
ims = []

for _ in range(T):
    u = step(u)
    im = plt.imshow(u, animated=True, cmap='hot')
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
plt.colorbar(im, orientation='horizontal')
plt.show()

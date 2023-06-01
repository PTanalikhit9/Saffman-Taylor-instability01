import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
N = 100
oil = 0
water = 1
prob_transition = 0.5

# Initialize the grid with oil and water at the center
grid = np.zeros((N, N), dtype=int)
grid[N // 2, N // 2] = water

# Define the CA rule
def rule(i, j, grid):
    if grid[i, j] == oil:
        neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        for neighbor in neighbors:
            ni, nj = neighbor
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if grid[ni, nj] == water:
                    if np.random.rand() < prob_transition:
                        return water
    return grid[i, j]

# Update the grid
def update(grid):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            new_grid[i, j] = rule(i, j, grid)
    return new_grid

# Set up the figure
fig, ax = plt.subplots()

# Animation update function
def animate(i):
    ax.clear()
    ax.imshow(grid, cmap='gray', interpolation='nearest')
    ax.set_title("Step {}".format(i))
    global grid
    grid = update(grid)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100)

plt.show()

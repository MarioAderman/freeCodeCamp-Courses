import matplotlib.pyplot as plt
import numpy as np

# Create a grid of points in 2D space
x_vals = np.linspace(-2, 2, 21)
y_vals = np.linspace(-2, 2, 21)
X, Y = np.meshgrid(x_vals, y_vals)

# Define two basis vectors for a vector space
# Try changing these vectors to see different bases
basis1 = np.array([1, 2])
basis2 = np.array([2, 1])

# Apply the basis transformation to the grid points
points = np.stack([X.ravel(), Y.ravel()])
transformed_points = basis1[:, None] * points[0] + basis2[:, None] * points[1]

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)

# Plot transformed grid
for i in range(len(x_vals)):
    ax.plot(transformed_points[0, i*len(y_vals):(i+1)*len(y_vals)],
            transformed_points[1, i*len(y_vals):(i+1)*len(y_vals)],
            color='lightblue', lw=1)
for j in range(len(y_vals)):
    ax.plot(transformed_points[0, j::len(y_vals)],
            transformed_points[1, j::len(y_vals)],
            color='lightblue', lw=1)

# Plot basis vectors
ax.quiver(0, 0, *basis1, angles='xy', scale_units='xy', scale=1, color='red', label='basis1')
ax.quiver(0, 0, *basis2, angles='xy', scale_units='xy', scale=1, color='green', label='basis2')

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
ax.set_title('Visualizing Basis Vectors and the Grid They Span')
plt.show()

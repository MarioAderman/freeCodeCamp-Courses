import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Transformation matrices
A_positive = np.array([[2, 1], 
                       [1, 2]])  # det = 3
A_negative = np.array([[0, 1], 
                       [1, 0]])  # det = -1
A_zero = np.array([[1, 1], 
                   [2, 2]])      # det = 0

matrices = [
    (A_positive, "Positive Determinant"),
    (A_negative, "Negative Determinant"),
    (A_zero, "Zero Determinant")
]

# Function to plot each transformation
def plot_case(A, ax, title):
    origin = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    unit_square = np.vstack([origin, origin[0]])
    transformed = unit_square @ A.T
    det_A = np.linalg.det(A)

    # Original unit square
    ax.plot(unit_square[:, 0], unit_square[:, 1], 'b--', label='Unit Square')
    ax.fill(unit_square[:, 0], unit_square[:, 1], color='lightblue', alpha=0.5)

    # Transformed shape
    ax.plot(transformed[:, 0], transformed[:, 1], 'r-', label='Transformed Shape')
    ax.fill(transformed[:, 0], transformed[:, 1], color='salmon', alpha=0.6)

    # Column vectors
    ax.quiver(0, 0, A[0, 0], A[1, 0], angles='xy', scale_units='xy', scale=1, color='purple', label='Column 1')
    ax.quiver(0, 0, A[0, 1], A[1, 1], angles='xy', scale_units='xy', scale=1, color='green', label='Column 2')

    ax.set_title(f"{title}\nDeterminant = {det_A:.2f}")
    ax.set_xlim(-2, 4)
    ax.set_ylim(-2, 4)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()

# Plot all three
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for ax, (A, title) in zip(axes, matrices):
    plot_case(A, ax, title)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define matrices
A_positive = np.array([[2, 1], [1, 2]])  # det = 3
A_negative = np.array([[0, 1], [1, 0]])  # det = -1

# Vertices of unit square in order (counterclockwise)
square_points = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
square_points_closed = np.vstack([square_points, square_points[0]])

def plot_with_labels(A, ax, title):
    transformed = square_points @ A.T
    transformed_closed = np.vstack([transformed, transformed[0]])
    det_A = np.linalg.det(A)

    # Original square
    ax.plot(square_points_closed[:, 0], square_points_closed[:, 1], 'b--')
    ax.fill(square_points_closed[:, 0], square_points_closed[:, 1], color='lightblue', alpha=0.3)

    for i, pt in enumerate(square_points):
        ax.text(pt[0]+0.05, pt[1]+0.05, str(i+1), color='blue')

    # Transformed shape
    ax.plot(transformed_closed[:, 0], transformed_closed[:, 1], 'r-')
    ax.fill(transformed_closed[:, 0], transformed_closed[:, 1], color='salmon', alpha=0.5)

    for i, pt in enumerate(transformed):
        ax.text(pt[0]+0.05, pt[1]+0.05, str(i+1), color='darkred')

    # Vectors (columns of A)
    ax.quiver(0, 0, A[0, 0], A[1, 0], angles='xy', scale_units='xy', scale=1, color='purple', label='Col 1')
    ax.quiver(0, 0, A[0, 1], A[1, 1], angles='xy', scale_units='xy', scale=1, color='green', label='Col 2')

    ax.set_title(f"{title}\nDeterminant = {det_A:.2f}")
    ax.set_xlim(-2, 3)
    ax.set_ylim(-2, 3)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

plot_with_labels(A_positive, ax1, "Positive Determinant (Orientation Preserved)")
plot_with_labels(A_negative, ax2, "Negative Determinant (Orientation Flipped)")

plt.tight_layout()
plt.show()

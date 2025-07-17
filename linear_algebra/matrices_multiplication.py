import numpy as np
import matplotlib.pyplot as plt

def plot_transformation(A, B=None):
    # Create basis vectors
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])

    # Apply matrix A (or B then A if B is provided)
    if B is not None:
        AB = A @ B
        Ai = A @ (B @ i_hat)
        Aj = A @ (B @ j_hat)
    else:
        AB = A
        Ai = A @ i_hat
        Aj = A @ j_hat

    # Plot settings
    fig, ax = plt.subplots()
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)
    ax.grid(True, linestyle='--')

    # Original basis
    ax.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='blue', label='î')
    ax.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='cyan', label='ĵ')

    # Transformed basis
    ax.quiver(0, 0, Ai[0], Ai[1], angles='xy', scale_units='xy', scale=1, color='red', label="T(î)")
    ax.quiver(0, 0, Aj[0], Aj[1], angles='xy', scale_units='xy', scale=1, color='orange', label="T(ĵ)")

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title(f"Transformation by matrix:\n{AB}")
    ax.legend()
    plt.show()

# Example usage:
A = np.array([[2, 1],
              [1, 3]])

B = np.array([[-1, 0],
              [0, -1]])

plot_transformation(A)        # Just A
plot_transformation(A, B)     # B followed by A (i.e., A * B)

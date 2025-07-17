import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the target transformation matrix
A = np.array([[2, 1],
              [1, 3]])

# Identity matrix (starting point)
I = np.eye(2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.axhline(0, color='gray', lw=1)
ax.axvline(0, color='gray', lw=1)
ax.grid(True, linestyle='--')

# Initial basis vectors
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])

# Initialize quiver objects (arrows)
quiver_i = ax.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='blue', label='î')
quiver_j = ax.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='cyan', label='ĵ')
quiver_ti = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='red', label='T(î)')
quiver_tj = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='orange', label='T(ĵ)')

ax.legend()

# Animation function
def animate(t):
    # Interpolate between identity and A
    M = (1 - t) * I + t * A
    ti = M @ i_hat
    tj = M @ j_hat

    # Update quivers
    quiver_ti.set_UVC(ti[0], ti[1])
    quiver_tj.set_UVC(tj[0], tj[1])
    return quiver_ti, quiver_tj

# Create animation: t from 0 to 1 in 60 frames
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 1, 60), interval=80, blit=True)

plt.show()

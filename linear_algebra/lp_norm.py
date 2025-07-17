import numpy as np
import matplotlib.pyplot as plt

p_values = [1, 2, 4, 10, np.inf]
theta = np.linspace(0, 2 * np.pi, 1000)

fig, ax = plt.subplots(figsize=(6,6))

for p in p_values:
    if p == np.inf:
        x = np.linspace(-1, 1, 100)
        y1 = np.ones_like(x)
        y2 = -np.ones_like(x)
        ax.plot(x, y1, 'k--')
        ax.plot(x, y2, 'k--')
        ax.plot(y1, x, 'k--')
        ax.plot(y2, x, 'k--')
    else:
        x = np.cos(theta)
        y = np.sin(theta)
        norm = (np.abs(x)**p + np.abs(y)**p)**(1/p)
        x_unit = x / norm
        y_unit = y / norm
        ax.plot(x_unit, y_unit, label=f"p={p}")

ax.set_aspect('equal')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.legend()
ax.set_title("Unit Norm Balls for Different p")
plt.grid(True)
plt.show()

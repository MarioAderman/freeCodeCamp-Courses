import matplotlib.pyplot as plt
import numpy as np

# Simulated data
y_true = np.array([300000, 320000, 340000, 360000, 380000, 400000])
y_pred = np.array([310000, 330000, 325000, 355000, 370000, 390000])
y_mean = np.mean(y_true)

# Errors
errors = y_true - y_pred
squared_errors = (y_true - y_pred) ** 2
absolute_errors = np.abs(y_true - y_pred)
sst = np.sum((y_true - y_mean) ** 2)
ssr = np.sum(squared_errors)
r2 = 1 - ssr / sst
mae = np.mean(absolute_errors)
rmse = np.sqrt(np.mean(squared_errors))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(y_true))

# Plot actual and predicted
ax.plot(x, y_true, 'o-', label='Actual (y_true)', color='blue')
ax.plot(x, y_pred, 's--', label='Predicted (y_pred)', color='orange')
ax.hlines(y_mean, xmin=-0.5, xmax=len(y_true)-0.5, colors='gray', linestyles='dotted', label='Mean of y (ȳ)')

# Draw error lines
for i in range(len(y_true)):
    ax.vlines(x[i], y_pred[i], y_true[i], color='red', linestyle='dashed', alpha=0.6)

# Labels and legend
ax.set_xticks(x)
ax.set_xticklabels([f"Point {i+1}" for i in x])
ax.set_title("Visualizing MAE, RMSE, and R²")
ax.set_ylabel("Target Value")
ax.legend()
ax.grid(True)

# Display MAE, RMSE, R²
textstr = f"MAE = {mae:.2f}\nRMSE = {rmse:.2f}\nR² = {r2:.4f}"
props = dict(boxstyle='round', facecolor='white', alpha=0.8)
ax.text(0.75, 0.1, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='bottom', bbox=props)

plt.tight_layout()
plt.show()

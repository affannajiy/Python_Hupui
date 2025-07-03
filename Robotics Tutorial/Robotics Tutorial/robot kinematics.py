import matplotlib.pyplot as plt
import numpy as np
x, y, theta = 0, 0, 0
v = 1.0
w = np.pi / 8
dt = 0.1
x_path, y_path = [x], [y]
for _ in range(100):
    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += w * dt
    x_path.append(x)
    y_path.append(y)
plt.plot(x_path, y_path, label="Robot Path")
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Simulated Robot Motion")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
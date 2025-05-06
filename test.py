import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Define the true sine function
y_sin = np.sin(x)

# Define the cubic approximation
y_approx = x - (x**3) / 6

# Plot both
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_approx, label='Cubic Approx: $x - x^3/6$', color='red', linestyle='--')

# Add labels and legend
plt.title('sin(x) vs. Cubic Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

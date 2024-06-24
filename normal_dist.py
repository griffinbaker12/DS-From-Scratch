import matplotlib.pyplot as plt
import numpy as np


def x_squared(x):
    return x**2


def exp_squared(x):
    return np.exp(x_squared(x))


# Use numpy to create a smooth range of x values
xs = np.linspace(-3, 3, 1000)

# Calculate y values for each function
y_x_squared = x_squared(xs)
y_exp_squared = exp_squared(xs)


# Print out values at every major x value (e.g., every 100th point)
print("x values\t x^2\t\t e^(x^2)")
print("---------------------------------------")
for i in range(0, len(xs), 100):
    print(f"{xs[i]:.2f}\t\t {y_x_squared[i]:.2f}\t\t {y_exp_squared[i]:.2f}")


# plt.plot(xs, [np.exp(x) for x in xs], "-", label="ex")
plt.plot(xs, x_squared(xs), "-", label="x^2")
plt.plot(xs, exp_squared(xs), "--", label="e^(x^2)")
plt.legend()
plt.title("x^2 vs e^(x^2)")
plt.xlabel("x")
plt.ylabel("y")
# Set limits for x and y axes
plt.xlim(-10, 10)
plt.ylim(0, 200)  # Adjust the y-axis limit as needed
plt.grid(True)
plt.show()

# Main thing that this shows is how much faster e^x^2 grows relative to x^2

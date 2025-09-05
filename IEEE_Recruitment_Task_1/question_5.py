import matplotlib.pyplot as plot
import numpy as np

# Generating the random numbers from normal distribution
nums = np.random.normal(loc=0.0, scale=1.0, size=1000)

# Using Gauss's formula for standard normal distribution to get prob. density values
x = nums
y = np.exp(-(x**2) / 2) / np.sqrt(2 * np.pi)

# Plotting the graph
plot.scatter(x, y)
plot.title("Normal Distribution Scatter Plot")
plot.xlabel("Numbers")
plot.ylabel("Probability Density")
plot.show()

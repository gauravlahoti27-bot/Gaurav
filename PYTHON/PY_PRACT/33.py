import numpy as np

# Create array
a = np.array([10, 20, 30, 40, 50])

# Mean
mean = np.mean(a)

# Median
median = np.median(a)

# Standard Deviation
std_dev = np.std(a)

# Variance
variance = np.var(a)

# For correlation, need two arrays
b = np.array([5, 15, 25, 35, 45])
correlation = np.corrcoef(a, b)

# Display results
print("Array:", a)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)

print("\nCorrelation Coefficient Matrix:\n", correlation)
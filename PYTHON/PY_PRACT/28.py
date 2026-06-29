import numpy as np

# Create array
a = np.array([0, 1, 2, 0, 3, 0, 4])

result = a[a != 0]

print("Original Array:", a)
print("Non-zero elements:", result)
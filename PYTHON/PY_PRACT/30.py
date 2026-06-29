import numpy as np

# Create 2D array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# Display elements using loops
print("Elements of 2D array:")
for i in range(a.shape[0]):      # rows
    for j in range(a.shape[1]):  # columns
        print(a[i][j], end=" ")
    print()
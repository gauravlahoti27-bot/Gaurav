import numpy as np
a = np.array([[1,2,3],
              [4,5,6]])
print("Original Array:\n", a)

print("Elements of the array:")
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(f"a[{i}][{j}] = {a[i][j]}")
import numpy as np

# Method 1 using arange
a = np.arange(2, 51, 2)
print("Even numbers array:", a)
#Method 2 using list comprehension
a = np.array([i for i in range(2,51,2)])
print("Even numbers array:", a)
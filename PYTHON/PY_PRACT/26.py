import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])
c = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])

#INDEXING
print("Indexing: ",a[0])
print("Indexing: ",b[1][0])
print("Indexing: ",c[0][1][0])
#Slicing 
print("Slicing: ",a[1:4])
print("Slicing: ",b[:,1:3])
print("Slicing: ",c[0:2,0:2,0:2])
#Reshaping
print("Reshaping: ",a.reshape(5,1)) 
print("Reshaping: ",b.reshape(2,3))
print("Reshaping: ",c.reshape(2,4))
import numpy as np
a = np.array(['Gaurav', 'Darsh', 'Aryan', 'Shivam'])
print("Original String Array:", a)

b = np.append(a, 'Kumar')
print("After Push:", b)

c = np.delete(b, -3)
print("After Pop:", c)

d = np.copy(a) 
print("Copied Array:", d)

if(d == a).all():
    print("Both arrays 'a' and 'd' are equal")
else:
    print("Arrays 'a' and 'd' are not equal")

e = np.arange(2,51,2)
print("Even numbers from 2 to 50:", e)
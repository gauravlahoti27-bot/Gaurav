import array

x = array.array('i',[])
print("How many elements you want to store? ",end="")
n = int(input())

for i in range(n):
    print('Enter element: ',end="")
    x.append(int(input()))
print("Original array: ",x)

print('Enter element to search: ',end="")
s = int(input())
flag = False
for i in range(n):
    if s == x[i]:
        print("Element found at index: ",i+1)
        flag = True
if flag == False:
    print("Element not found in the array")
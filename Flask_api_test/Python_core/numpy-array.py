from numpy import *
arr=array([])
n=int(input("Enter the length of array: "))
for i in range(n):
    x=int(input("Enter the value: "))
    arr=append(arr,x)

print(arr)

val=int(input("Enter the value to search: "))
for i,val in enumerate(arr):
    if i==val:
        print("Value found at index: ",i)
        break
else: print("Value not found")
import numpy as np
x=[1,2,3,4]
print(x)
ar=np.array(x)
print(ar)
ar1=np.array([1,2,3,4,5])
print(ar1)
ar1
print(type(ar1))
print(ar1.ndim)
# ar1 was 1-d array
ar2=np.array([[1,2,3,4],[1,2,3,4]])
print(ar2)
print(ar2.ndim)
#ar2 is 2-D array
ar3=np.array([[[1,2,3,4], [1,2,3,4], [1,2,3,4]]])
print(ar3)
print(ar3.ndim)
#ar3 is 3-D array
arn=np.array([1,2,3,4], ndmin=10)# to create multidimensional array
print(arn)
print(arn.ndim)
print(ar3.dtype)
print(ar3.shape)
rng=np.arange(1,6)
print(rng)
lspace=np.linspace(1,50,10)
print(lspace)
emp=np.empty((4,6))
print(emp)
ide=np.identity(45)
print(ide)
arr=np.arange(99)
print(arr.reshape(3,33))
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.sum(axis=0))
print(arr1.sum(axis=1))
print(arr1.T)#transpose the array
for i in arr1.flat:
    print(i)
print(arr1.size)#returns the size of the array
print(arr1.nbytes)#returns the total bytes pf data present in the array
arr2=np.array([1,26,387,71])
print(arr2.argmax())#returns the index where the maximum value is present
print(arr2.argmin())#returns the index where the minimum value is present
print(arr2.argsort())#returns the index for the increasing order of value where they are present    
import numpy as np

arr = np.array([1,2,3,4,"test"])
print(arr)

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,0]])
print(arr2)

#arr3 = np.array([[[1,2,3], [6,7,8,], [2,2,2]],[1,2,3],[2,2,2][2,2,2]])
#print(arr3)

print(arr.ndim)
print(arr2.ndim)
#print(arr3.ndim)

arr4 = np.array([1,2,3,4,5], ndmin=5)
print(arr4)

print(arr[1])
print(arr2[1][2])

print(arr.dtype)
print(arr2.dtype)

arr5 = np.array([1,2,3,4,5], dtype="str")
print(arr5)

a = bytearray(5)
print(a)

arr3 = np.array([[[1,2],[2,3]],
                 [[1,2],[2,3]]
                 ])
print(arr3.shape)
print(arr3.ndim)

#reshape

ar = np.array([1,2,3,4,5,6,7,8,9,0])
print(ar.reshape(2,5))

for i in np.nditer(arr2):
    print(i)

con1 = np.array([[1,2,3,4],[5,6,7,8]])
con2 = np.array([[11,12,13,14],[15,16,17,18]])

con3 = np.concatenate((con1,con2),axis=1)
print(con3)

con4 = np.stack((con1,con2),axis=1)
print(con4)
print(con4.ndim)
print(con4.shape)

#split

splitarr = np.array([1,2,3,4,5,6,7,8,9,0])
print(np.array_split(splitarr, 11))

sortarr1 = np.array([6,9,1,4,9])
sortarr2 = np.array(["solo",1,3,4,"yolo"])

print(np.sort(sortarr1))
print(np.sort(sortarr2))
print(np.sort(sortarr1)[::-1])

#filter

original = np.array([1,2,3,4,5])
x = [True,False,False,True,False]
print(original[x])



#Distance between two points denotes similar values

''' Euclidean distance - shortest distance between 2 points
    Formula = root of ((x1-x2)**2 + (y1-y2)**2)) and it goes on
    Generic formula Summazation of n and n-1 ((pi-qi)2)1/2
'''

from scipy.spatial import distance
point1 = [1,2]
point2 = [4,5]
EuclideanDist = distance.euclidean(point1,point2)
print(EuclideanDist)

#manual calculation
a = (2, 3, 6)
b = (5, 7, 1)
x1,y1,z1 = 2,3,6
x2,y2,z2 = 5,7,1
Eucdist = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
print("manual ",Eucdist)

'''Manhattan distance - path goes linear
formula = |p1-p2| + |q1-q2|
'''
manhattanDist = distance.cityblock(point1,point2)
print(manhattanDist)

#manual calculation
manhat = sum(abs(point1-point2) for point1, point2 in zip(point1,point2))
print("manual ",manhat)

'''Hamming distance'''
str1 = "MEXICON"
str2 = "MECIQAN"

hamming_distance = distance.hamming(list(str1), list(str2))*len(str1)
print(hamming_distance)
i=0
count = 0

for x in str1:
    if(str1[i]!=str2[i]):
        count = count + 1
    i = i+1
print(count)


#Distance between two points denotes similar values

''' Euclidean distance - shortest distance between 2 points
    Formula = root of ((p1-q1)2 + (p2-q2)) and it goes on
    Generic formula Summazation of n and n-1 ((pi-qi)2)1/2
'''

from scipy.spatial import distance
point1 = [1,2]
point2 = [4,5]
EuclideanDist = distance.euclidean(point1,point2)
print(EuclideanDist)

'''Manhattan distance - path goes linear
formula = |p1-p2| + |q1-q2|
'''
manhattanDist = distance.cityblock(point1,point2)
print(manhattanDist)

'''Hamming distance'''
str1 = "MEXICON"
str2 = "MEXIQAN"

hamming_distance = distance.hamming(list(str1), list(str2))*len(str1)
print(hamming_distance)



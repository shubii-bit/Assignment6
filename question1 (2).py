




import numpy as np
from numpy import linalg

# Creating a 2X2 matrix
A = np.array([[2 , 3 , 10],[4,-6, 5],[6 , 9 , -20]])

B = np.array([[4],[1],[2]])

print("Original 2-D matrix")
print(A,"\n")

# Output
print("Determinant of the 2-D matrix:")
print(np.linalg.det(A))
print("Therefore the system of eqations have some solution")

#inverse of the matrix given
A_inverse = np.linalg.inv(A)
#the inverse would be as fllows
print(A_inverse)

C = A_inverse.dot(B)
print(C)

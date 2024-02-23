########
##day5##
########
"""
-----Scipy------
"""

##a. Define a matrix A
matrixA = np.matrix(np.arange(1,10).reshape(3,3))
matrixA
#matrix([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
##wrong!!!
matrixA=np.matrix([[1,-2,3],[4,5,6],[7,8,9]])



##b.Define a vector b
vectorb = np.arange(1,4)


##c. Solve the linear system of equations A x = b
x = linalg.solve(matrixA, vectorb)
x
array([ 2.30695693e-16, -3.53252781e-17,  3.33333333e-01])

##d. Check that your solution is correct by plugging it into the equation
np.dot(matirxA, x) == vectorb
#matrix([[False,  True,  True]])

##e. Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)
matrixB = np.matrix(np.random.random(9).reshape(3,3))
x = linalg.solve(matrixA, matrixB)
np.dot(matrixA, x) == b

##f. Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
eg_val, eg_vect = linalg.eig(matrixA)
print(eg_val); print(eg_vect)

##g. Calculate the inverse, determinant of A
linalg.det(matrixA) #calculate determinant
np.dot(A, linalg.inv(matirxA)) # calculate and check the inverse and check it

##h. Calculate the norm of A with different orders
linalg.norm(matrixA, "fro")
"""
16.881943016134134
"""
linalg.norm(matrixA, "nuc")
"""
20.42215916111805
"""

"""
--------Statistics---------
"""

from scipy import stats
import numpy as np

# Test if two sets of (independent) random data comes from the same distribution
tats.norm.rvs(size=1000)
var2 = stats.norm.rvs(size=1000)
stats.ttest_ind(var1,var2)
#TtestResult(statistic=-0.3934207168361582, pvalue=0.694050746846733, df=1998.0)



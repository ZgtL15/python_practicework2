import numpy as np

##a. Create a null vector of size 10 but the fifth value which is 1

null_array = np.zeros(10)
null_array[4] = 1
###>>> null_array
###array([0., 0., 0., 0., 1., 0., 0., 0., 0., 0.])

###b. Create a vector with values ranging from 10 to 49
 
range_value=np.arange(10,50)
###>>>range_value
#array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
#       44, 45, 46, 47, 48, 49])

###c. Reverse a vector (first element becomes last)
range_value_t=range_value[::-1]
###>>> range_value_t
###array([49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33,
#       32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
#       15, 14, 13, 12, 11, 10])


###d. Create a 3x3 matrix with values ranging from 0 to 8
matrixA=np.arange(9).reshape(3,3)
matrixB=np.matrix(np.arange(9).reshape(3,3))##this is the right one!
###matirx23
#array([[0, 1, 2],
#       [3, 4, 5],
#       [6, 7, 8]])



###e. Find indices of non-zero elements from [1,2,0,0,4,0]
a=[1,2,0,0,4,0]
b=np.array(a)
c=b>0
b[c]#what we need!

###f.Create a random vector of size 30 and find the mean value
np_randome = np.random.random((30))
np.mean(np_randome)## the mean value
##also!!! we can do 
np.median(np_randome)#......and a lot, really usefule!

###g. Create a 2d array with 1 on the border and 0 inside
np_2d_array = np.zeros((3,3))
np_2d_array[0,:] = 1 #change first row to 1
np_2d_array[-1,:] = 1 #change last row to 1
np_2d_array[:, 0] = 1 #change first col to 1
np_2d_array[:,-1] = 1 #change last col to 2
np_2d_array # down!
#array([[1., 1., 1.],
#       [1., 0., 1.],
#       [1., 1., 1.]])

###h. Create a 8x8 matrix and fill it with a checkerboard pattern
array_r = np.array([[0,1], [1,0]])
matrix_cb = np.tile(array_r, (4,4))

###j. Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
np.negative(Z[4:8]
#----another way---- it is stupid but work!
for i in Z:
    if (i>3) and (i<8):
        Z[i]=-i

###k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
np.sort(Z)

###l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
np.array_equal(A,B)

###m. How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)















)





















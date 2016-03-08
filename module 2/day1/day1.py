import numpy as np
from scipy import linalg
A = np.array([[2,1],
              [3,-1],
              [0,4]])
v = np.array([-2,1])

# 1
print "Question 1"
# a
print "A.v = " + str(A.dot(v))

# b
print "{}.{} = {}".format(A[1:2,:], v, A[1:2,:].dot(v))

# c
# print A[:, 2:4].dot(v)

# 2
print ""
print "Question 2"
i2 = np.identity(2)
v2 = v
print "{}.{} = {}".format(i2, v2, i2.dot(v2))

# 3
print ""
print "Question 3"
t3 = np.array([[1,0,0],[0,1,0],[0,0,0]])
v3 = np.array([1,2,3])
print "{}.{} = {}".format(t3, v3, t3.dot(v3))

# 4
print ""
print "Question 4"
t4 = np.array([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
v4 = np.array([1,2,3,4])
print "{}.{} = {}".format(t4, v4, t4.dot(v4))

# 5
print ""
print "Question 5"

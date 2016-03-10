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

# 8
print ""
print "Question 8"
t8 = np.array([[3,0,0],[0,3,0],[0,0,3]])
v8 = np.array([2,2,2])
print "{}.{} = {}".format(t8, v8, t8.dot(v8))

# 9
print ""
print "Question 9"
t9 = np.array([[3,0,0],[0,5,0],[0,0,1]])
v9 = np.array([2,2,2])
print "{}.{} = {}".format(t9, v9, t9.dot(v9))

# 10
print ""
print "Question 10"
t10 = np.array([[0,1,0],[-1,0,0],[0,0,1]])
v10_1 = np.array([1,0,0])
v10_2 = np.array([0,1,0])
v10_3 = np.array([0,0,1])

print "{}.{} = {}".format(t10, v10_1, t10.dot(v10_1))
print "{}.{} = {}".format(t10, v10_2, t10.dot(v10_2))
print "{}.{} = {}".format(t10, v10_3, t10.dot(v10_3))
print "This rotation matrix is rotating the x and y elements by 90 degrees"

# 11
print ""
print "Question 11"
t11 = np.array([[1,0,0],
                [0,0,-1],
                [0,1,0]])
v11_1 = np.array([1,0,0])
v11_2 = np.array([0,1,0])
v11_3 = np.array([0,0,1])

print "{}.{} = {}".format(t11, v11_1, t11.dot(v11_1))
print "{}.{} = {}".format(t11, v11_2, t11.dot(v11_2))
print "{}.{} = {}".format(t11, v11_3, t11.dot(v11_3))

# 12, 13, 14, 15, 16
print ""
print "Question 12, 13, 14, 15, 16"
angleDeg12 = 30
q12 = angleDeg12 * (np.pi / 180) #30 degrees to radians
t12 = np.array([[np.cos(q12),np.sin(q12),0],[-np.sin(q12),np.cos(q12),0],[0,0,1]])
v12_1 = np.array([1,0,0])
dot12 = t12.dot(v12_1)
mag12 = (dot12[0]**2 + dot12[1]**2 + dot12[2]**2)**(1/2)
print "Angle degrees, q12 = {}".format(angleDeg12)
print "{}.{} = {}".format(t12, v12_1, dot12)
print "This rotation matrix is rotating the x and y elements by q12 degrees"
print "magnitude of vector = {} = {}".format("SQRT(a^2 + b^2 + c^2)",mag12)
print "this matrix will rotate in x, y by given number of degrees in the negative direction"

# 17
print ""
print "Question 17"
A17 = np.array([[-2,4],
                [0,3]])
B17 = np.array([[5,-3],
                [-1,-1]])
C17 = A17.dot(B17)
print "{}\t{}\t= {}".format(A17[0], B17[0], C17[0])
print "{}\t{}\t= {}".format(A17[1], B17[1], C17[1])

# 18
print ""
print "Question 18"
A18 = np.array([[-2,4],
                [0,3]])
B18 = np.array([[5,-3],
                [-1,-1]])
C18 = B18.dot(A18)
print "{}\t  {} = {}".format(B18[0], A18[0], C18[0])
print "{}\t. {}   = {}".format(B18[1], A18[1], C18[1])

# 17
print ""
print "Question 17"
A19 = np.array([[-2,4],
                [0,3]])
B19 = np.array([[5,-3],
                [-1,-1]])
C19 = np.array([[-5,-1],
                [-3,2]])
D19 = A19.dot(B19+C19)
print "{}\t   | {}\t \t{} | = {}".format(A19[0], B19[0], C19[0], D19[0])
print "{}  \t . | {}\t+\t{} | = {}".format(A19[1], B19[1], C19[1], D19[1])

# 22 
print ""
print "Question 22" 
angleDeg22 = 30
q22 = angleDeg22 * (np.pi / 180) #30 degrees to radians
t22 = np.array([[np.cos(q22),np.sin(q22),0],[-np.sin(q22),np.cos(q22),0],[0,0,1]])
v22_1 = np.array([1,0,0])
dot22 = t22.dot(v22_1)
print "Angle degrees, q22 = {}".format(angleDeg22)
print "{}.{} = {}".format(t22, v22_1, dot22)
print ""

angleDeg22b = -30
q22b = angleDeg22b * (np.pi / 180) #30 degrees to radians
t22b = np.array([[np.cos(q22b),np.sin(q22b),0],[-np.sin(q22b),np.cos(q22b),0],[0,0,1]])
dot22b = t22b.dot(dot22)
print "Angle degrees, q22b = {}".format(angleDeg22b)
print "{}.{} = {}".format(t22b, dot22, dot22b)
print ""

dot22c = t22.dot(t22b)
print "{}\t {} = {}".format(t22b[0], t22b[0], dot22c[0])
print "{}\t {} = {}".format(t22b[1], t22b[1], dot22c[1])
print "{}\t\t\t\t.{}\t\t\t    = {}".format(t22b[2], t22b[2], dot22c[2])

print "rotation matrix * rotation backwards = identity matrix" 

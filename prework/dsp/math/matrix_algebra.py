# Import numpy and create all matrices from assignment
import numpy as np

A = np.array([[1, 2, 3], [2, 7 ,4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

# Section 1) Matrix Dimensions
print '1.1) A', np.shape(A)                 # 1.1) 2x3
print '1.2) B', np.shape(B)                 # 1.2) 2x2
print '1.3) C', np.shape(C)                 # 1.3) 3x2
print '1.4) D', np.shape(D)                 # 1.4) 2x3
print '1.5) u', np.shape(u)                 # 1.5) One dimension; 4 elements
print '1.6) w', np.shape(w)                 # 1.6) 4x1

# Section 2) Vector Operations
print '\n2.1)', u + v                                   # 2.1) [9  7 -4  9]
print '2.2)', u - v                                     # 2.2) [3 -3 -2  1]
print '2.3)', 6*u                                       # 2.3) [36  12 -18  30]
print '2.4)', np.dot(u, v)                              # 2.4) 51
print '2.5)', np.linalg.norm(u)                         # 2.5) 8.60 (sqrt(74))

# Section 3) Matrix Operations
try: print '\n3.1)\n', A + C                            # 3.1) undefined
except: print 'undefined'

try: print '\n3.2)\n', A - C.transpose()                # 3.2) [[-4 -7 -3]
except: print 'undefined'                               #       [ 3  6  4]]

try: print '\n3.3)\n', C.transpose() + (3*D)            # 3.3) [[14  3  3]
except: print 'undefined'                               #       [ 2  7  9]]

try: print '\n3.4)\n', np.dot(B, A)                     # 3.4) [[-1 -5 -1]
except: print 'undefined'                               #       [ 2  7  4]]

try: print '\n3.5)\n', np.dot(B, A.transpose())         # 3.5) undefined
except: print 'undefined'

# Optional Section
try: print '\n3.6)\n', np.dot(B,C)                      # 3.6) undefined
except: print 'undefined'

try: print '\n3.7)\n', np.dot(C,B)                      # 3.7) [[ 5 -6]
except: print 'undefined'                               #       [ 9 -8]
                                                        #       [ 6 -6]]

try: print '\n3.8)\n', np.dot(np.dot(np.dot(B,B),B),B)  # 3.8) [[ 1 -4]
except: print 'undefined'                               #       [ 0  1]]

try: print '\n3.9)\n', np.dot(A, A.transpose())         # 3.9) [[14 28]
except: print 'undefined'                               #       [28 69]]

try: print '\n3.10)\n', np.dot(D.transpose(), D)        # 3.10) [[10 -4  0]
except: print 'undefined'                               #        [-4  8  8]
                                                        #        [ 0  8 10]]

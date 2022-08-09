import numpy as np

# print(np.__version__)


# a= np.zeros(10)
# print(a)

# print(a.itemsize)

# x=np.zeros(10)
# x[4]=1
# print(x)

# v = np.arange(10,49)
# y=v[::-1]
# print(y)

# l =  np.arange(0, 9).reshape(3,3)
# print(l)

# e = np.array([1,2,0,0,4,0])
# print(np.nonzero(e))

# print(np.identity(3))

# t = np.random.random((3,3,3))
# print(t)


# x = np.random.randint(1,15,(10,10))
# print("Original Array:")
# print(x) 
# xmin, xmax = x.min(), x.max()
# print("Minimum and Maximum Values:")
# print(xmin, xmax)

# x = np.random.randint(1,10,(30))
# print(x.mean())

# l= np.zeros(10)
# l[0]=1
# l[-1]=1
# print(l) 

# x = np.ones((3,3))
# print("Original array:")
# print(x)
# print("0 on the border and 1 inside in the array")
# x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
# print(x)

#nan
#false
#false
#nan
# print(0.3 == 3 * 0.1)

# x = np.diag([1, 2, 3, 4, 7])
# print(x)

# x = np.ones((1,1))
# print("Checkerboard pattern:")
# x = np.zeros((8,8),dtype=int)
# x[1::2,::2] = 1
# x[::2,1::2] = 1
# print(x)



# print(np.unravel_index(99,(6,7,8)))


# Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
# print(Z)

# w=np.tile( np.array([[0,1],[1,0]]), (4,4))
# print(w)

# Z = np.random.random((5,5))
# Z = (Z - np.mean (Z)) / (np.std (Z))
# print(Z)

# color = np.dtype([("r", np.ubyte),
#                   ("g", np.ubyte),
#                   ("b", np.ubyte),
#                   ("a", np.ubyte)])
# print(color)


# Z = np.dot(np.ones((5,3)), np.ones((3,2)))
# print(Z)

# Z = np.arange(11)
# Z[(3 < Z) & (Z <=8)] *= -1
# print(Z)

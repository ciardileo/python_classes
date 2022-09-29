import numpy as n

# creating a array

array = n.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # dtype = choose the type of data

# accumulated sum

print(array.cumsum())

print(array[0])

array[2] = 12

# the arrays has more functions than lists, but only can keep one type of element

# create a array following a arithmetic progression

print(n.arange(1, 4, 0.5))  # start, end, step

# creates a array filled by zeros

empty_array = n.zeros(10)  # quantity
print(empty_array)

# number of lines and columns (X, Y)

print(n.shape(empty_array))

# returns 1 in the diagonals and 0 in the rest

z = n.eye(3)  # number of lines and columns
print(z)

# form a matrix in diagonal

print(n.diag(n.array([1, 2, 3, 4])))

# creates a matrix (list organized by lines and columns) filled by ones

one_matrix = n.ones((2, 3))  # line, columns
print(one_matrix)

lists = [[10, 2, 3], [12, 4, 67]]

# transforms in a matrix

matrix_list = n.matrix(lists)

# like a len()

print(n.size(matrix_list))

# item size (in bits)

# print(n.itemsize(matrix_list))

# total bytes

# print(matrix_list.nbytes())

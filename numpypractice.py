import numpy as np
arr = np.array([1,2,3,4,5,6])
new_arr = arr.reshape(2,3)
print(new_arr)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
new_arr = arr.reshape(3,3)
print(new_arr)

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
new_matrix = matrix.flatten()
print(new_matrix)

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
new_matrix = matrix.ravel()
print(new_matrix)

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
new_matrix = matrix.transpose()
print(new_matrix)

import numpy as np
matrix = np.zeros((2,3))
print(matrix)

import numpy as np
matrix = np.ones((3,2))
print(matrix)

import numpy as np
matrix = np.full((2,4), 7)
print(matrix)

import numpy as np
matrix = np.arange(2,21,2)
print(matrix)

import numpy as np
matrix = np.linspace(0,10,5)
print(matrix)

import numpy as np
a = np.array([1, 2, 3])
b = (np.array([4, 5, 6]))
new_matrix = np.concatenate((a, b))
print(new_matrix)

import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
vstack = np.vstack((a, b))
hstack = np.hstack((a, b))
print(vstack)
print(hstack)

import numpy as np
marks = np.array([
    [65, 80, 75],
    [90, 55, 85],
    [40, 70, 60],
    [88, 92, 95]
])
print(marks[1])
print(marks[:,0])
print(marks[marks > 80])
print(marks.shape)

import numpy as np
data = np.arange(1, 13)
print(data.reshape(3, 4))
transpose =np.transpose(data)
flattened =transpose.flatten()
print(flattened)
print(flattened.shape)

import numpy as np

features = np.array([
    [20, 50000],
    [25, 60000],
    [30, 75000],
    [35, 90000],
    [40, 100000]
])
print(features[features > 25])
print(features[:,1])
print(features[features[:,1] > 75000])
print(features[:,1].reshape(5,1))
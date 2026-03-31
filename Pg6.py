import numpy as np 
# Creating a 1D NumPy array  
array_1d = np.array([1, 2, 3, 4, 5, 6])  
print("1D Array:") 
print(array_1d) 
# Reshaping the 1D array to a 2x3 2D array  
array_2d = array_1d.reshape(2, 3)  
print("\nReshaped to 2D Array (2x3):")  
print(array_2d) 
# Accessing elements using indexing  
print("\nElement at position (1, 2):", array_2d[1, 2]) 
# Modifying an element  
array_2d[0, 1] = 10 
print("\nModified Array (After changing element at position (0,1) to 10):")
print(array_2d) 
# Calculating the sum of the array elements  
array_sum = np.sum(array_2d) 
print("\nSum of all elements in the array:", array_sum)

import numpy as np 
# Creating two matrices 
matrix_A = np.array([[1, 2], [3, 4]]) 
matrix_B = np.array([[5, 6], [7, 8]]) 
# Matrix Addition 
matrix_sum = np.add(matrix_A, matrix_B)  
print("Matrix Addition (A + B):")  
print(matrix_sum) 
# Matrix Multiplication (Element-wise)  
matrix_product_elementwise = np.multiply(matrix_A, matrix_B)
print("\nElement-wise Matrix Multiplication (A * B):")  
print(matrix_product_elementwise) 
# Matrix Dot Product (Matrix Multiplication)  
matrix_dot_product = np.dot(matrix_A, matrix_B)  
print("\nMatrix Dot Product (A . B):")  
print(matrix_dot_product) 


import numpy as np

print("installed numpy and learning")

numbers= np.array([1,2,3,4,5])

print("array is " ,  numbers)
print("maximum is" , max(numbers))
print("minimum is " , min(numbers))

print("mean is  ", np.mean(numbers))
print("standard devition " , np.std(numbers))

matrix= np.array([[1,2,3],[4,5,6]])

print("matrix is:\n ", matrix)
print("Matrix Shape:", matrix.shape)
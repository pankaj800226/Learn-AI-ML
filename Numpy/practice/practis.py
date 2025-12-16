import numpy as np


#normal python list code
list = [1,2,3,4,5]
print(list)

# numpy code 
p = np.array([1, 2, 3, 4, 5])
print(p)

a2_Array = np.array([[1,2,6],
                     [3,5,3]])
print(a2_Array)

print("3D array")
array3d = np.array([[[1,2,3],
                     [2,5,4]],  
                     [[2,3,4],
                     [3,5,6]]])
print(array3d)


arange = np.arange(10)
print(arange*2)

import numpy as np

array = np.array([1,2,3,4,5,6])
insert_value = np.insert(array,3,1000)
print("original array", array)
print("insert value : ", insert_value)
append = np.append(array,[20,30,40])
print("append value ",append) 

delete_value = np.delete(array,0)
print("delete ",delete_value)

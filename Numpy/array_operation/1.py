import numpy as np
# slicing array
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("basic slice",arr[2:9])
print("with step slice",arr[2:9:2])

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,15]]) 
print("specifuc element : ",arr_2d[0,2])
print("Entire row : ",arr_2d[0]) # jis index ko chaho us ko target kr skte ho
print("all matrix : ",arr_2d[:])
print("Entire row 2 : ",arr_2d[2])

# sorting array
unsorted = np.array([2,1,3,5,4,6,9,7])
print("Sorted Array : ",np.sort(unsorted))


# 2d sorting array

arr_2dSotred = np.array([[2,4,2],[9,0,8],[5,7,3]])
print("2d sorted array :", np.sort(arr_2dSotred))
print("type array",arr_2dSotred.ndim)


# Filter in array
# even number

number = np.array([1,2,3,4,5,6,7,8,9])
even_numver = number[number % 2 == 0]
print(even_numver)
print("sharp :",number.ndim)



mask = number > 5 # number me jo 5 se upar ka value he o filter krta he
print(number[mask])

condition_array = np.where(number > 5,number*2, number)
print("condition : ", condition_array)


# add and remove data 

concateArray1 = np.array([1,2,3])
concateArray2 = np.array([4,5,6,7])
concate = np.concatenate((concateArray1,concateArray2))
print(concate)


# competibility 
a = np.array([1,2,3])
b = np.array([4,5,6])
print("competibility", a.shape== b.shape)


# delete 
deleted_array = np.array([1,2,3,4,5,6])
delete = np.delete(deleted_array,2)
print("Deleted value in array : ",delete)

# add element value in array 
firstArray = np.array([[1,2],[3,4]])
new_row = np.array([[8,9]]) # row wise added
# new_row = np.array([18,19])

res = np.vstack((firstArray,new_row))
print("Row add ",res)

# column wise add
new_col = np.array([[7],[8]])
res2 = np.hstack((firstArray,new_col))
print("Column add ",res2)


array1 = np.array([1,2,3,4])
np.save('array1.npy',array1)

load_array = np.load('array1.npy')
print(load_array) 








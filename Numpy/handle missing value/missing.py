import numpy as np 


# check missing value in array
arr = np.array([1,2, np.nan,4,5, np.nan])
print(arr)
print(np.isnan(arr))

# handle missing value and solve missing value
print(np.nan_to_num(arr,nan=10))

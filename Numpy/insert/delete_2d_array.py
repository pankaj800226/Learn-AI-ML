import numpy as np

remove2dArray = np.array([[1,2,3], [4,5,6]])

delete = np.delete(remove2dArray,0 ,axis=0)
print("delete",delete)
print(remove2dArray.shape)
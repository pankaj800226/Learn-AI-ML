# default value 
import numpy as np

#zero value 
a = np.zeros(3)
print(a)

# ones value shape start
b = np.ones((2,4))
print(b)


# user defined value of  throuth 8 is a default value
c = np.full((2,3),8)
print(c)


#sequence number
#arange(start,stop,step)
d = np.arange(5) # 1 se 4 tk
d2 = np.arange(1,10) #1 se 10 tk
d3 = np.arange(1,10,2) # 1 start stop 9  and 2 is 1 - kam karega 
print(d)
print(d2)
print(d3)

# identity matrices

e = np.eye(3) # 3 means 3 ka row 
print("eye: " ,e)

# randome number 
random = np.random.random([2,3])
print(random)






